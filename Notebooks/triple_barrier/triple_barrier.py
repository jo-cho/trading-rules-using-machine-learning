import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

def add_vertical_barrier(t_events, close, days=0, hours=0, minutes=0, seconds=0):
    """
    Advances in Financial Machine Learning, Snippet 3.4 page 49.
    Adding a Vertical Barrier
    For each index in t_events, it finds the timestamp of the next price bar at or immediately after
    a number of days num_days. This vertical barrier can be passed as an optional argument t1 in get_events.
    This function creates a series that has all the timestamps of when the vertical barrier would be reached.
    :param t_events: (pd.Series) Series of events (symmetric CUSUM filter)
    :param close: (pd.Series) Close prices
    :param num_days: (int) Number of days to add for vertical barrier
    :param num_hours: (int) Number of hours to add for vertical barrier
    :param num_minutes: (int) Number of minutes to add for vertical barrier
    :param num_seconds: (int) Number of seconds to add for vertical barrier
    :return: (pd.Series) Timestamps of vertical barriers
    """
    timedelta = pd.Timedelta(
        '{} days, {} hours, {} minutes, {} seconds'.format(days, hours, minutes, seconds))
    # Find index to closest to vertical barrier
    nearest_index = close.index.searchsorted(t_events + timedelta)

    # Exclude indexes which are outside the range of close price index
    nearest_index = nearest_index[nearest_index < close.shape[0]]

    # Find price index closest to vertical barrier time stamp
    nearest_timestamp = close.index[nearest_index]
    filtered_events = t_events[:nearest_index.shape[0]]

    vertical_barriers = pd.Series(data=nearest_timestamp, index=filtered_events)
    return vertical_barriers


def forming_barriers(close, events, pt_sl, molecule): 
    """
    Advances in Financial Machine Learning, Snippet 3.2, page 45.
    Triple Barrier Labeling Method
    This function applies the triple-barrier labeling method. It works on a set of
    datetime index values (molecule). This allows the program to parallelize the processing.
    Mainly it returns a DataFrame of timestamps regarding the time when the first barriers were reached.
    :param close: (pd.Series) Close prices
    :param events: (pd.Series) Indices that signify "events" (see cusum_filter function
    for more details)
    :param pt_sl: (np.array) Element 0, indicates the profit taking level; Element 1 is stop loss level
    :param molecule: (an array) A set of datetime index values for processing
    :return: (pd.DataFrame) Timestamps of when first barrier was touched
    """
    # Apply stop loss/profit taking, if it takes place before t1 (end of event)
    events_ = events.loc[molecule]
    out = events_[['exit']].copy(deep=True)

    profit_taking_multiple = pt_sl[0]
    stop_loss_multiple = pt_sl[1]

    # Profit taking active
    if profit_taking_multiple > 0:
        profit_taking = profit_taking_multiple * events_['trgt']
    else:
        profit_taking = pd.Series(index=events.index)  # NaNs

    # Stop loss active
    if stop_loss_multiple > 0:
        stop_loss = -stop_loss_multiple * events_['trgt']
    else:
        stop_loss = pd.Series(index=events.index)  # NaNs

    out['pt'] = pd.Series(dtype=events.index.dtype)
    out['sl'] = pd.Series(dtype=events.index.dtype)

    # Get events
    for loc, vertical_barrier in events_['exit'].fillna(close.index[-1]).iteritems():
        closing_prices = close[loc: vertical_barrier]  # Path prices for a given trade
        cum_returns = (closing_prices / close[loc] - 1) * events_.at[loc, 'side']  # Path returns
        out.at[loc, 'sl'] = cum_returns[cum_returns < stop_loss[loc]].index.min()  # Earliest stop loss date
        out.at[loc, 'pt'] = cum_returns[cum_returns > profit_taking[loc]].index.min()  # Earliest profit taking date

    return out


def get_barrier(close, enter, pt_sl, max_holding, target=None, side=None):
    """

    :param close: (pd.Series) Close prices
    :param enter: (pd.Series) of entry points. These are timestamps that will seed every triple barrier.
        These are the timestamps
    :param pt_sl: (2 element array) Element 0, indicates the profit taking level; Element 1 is stop loss level.
        A non-negative float that sets the width of the two barriers. (if target is not None, pt_sl is ratio)
    :param target: (pd.Series) target rate
    :param max_holding: (2 element list) [days, hours]
    :param side: (pd.Series) Side of the bet (long/short) as decided by the primary model.
        1 if long, -1 if short
    :return: (pd.DataFrame) Events
            -events.index is event's starttime
            -events['exit'] is event's endtime
            -events['side'] implies the algo's position side
            -events['ret'] is return of each bet
    """

    # 1) Get target
    if target is None:
        target_ = pd.Series(1,index=enter)
    
    else:
        target_ = target.reindex(enter)

    # 2) Get vertical barrier (max holding period)
    vertical_barrier = add_vertical_barrier(enter, close, days=max_holding[0], hours=max_holding[1])

    # 3) Form events object, apply stop loss on vertical barrier
    if side is None:
        side_ = pd.Series(1.0, index=target_.index)
        pt_sl_ = [pt_sl[0], pt_sl[1]]
    else:
        side_ = side.reindex(target_.index)  # Subset side_prediction on target index.
        pt_sl_ = pt_sl[:2]

    # Create a new df
    events = pd.concat({'exit': vertical_barrier, 'trgt': target_,'side': side_}, axis=1)

    # Apply Triple Barrier
    first_touch_dates = forming_barriers(close, events, pt_sl_, events.index)
    

    for ind in events.index:
        events.at[ind, 'exit'] = first_touch_dates.loc[ind, :].dropna().min()

    events_x = events.dropna(subset=['exit'])

    out_df = pd.DataFrame(index=events.index)
    out_df['exit'] = events['exit']
    out_df['price'] = close
    out_df['ret'] = 0
    out_df.loc[events_x.index,'ret'] = (np.log(close.loc[events_x['exit'].array].array) - np.log(close.loc[events_x.index])) * events['side']
    out_df['side'] = events['side']
    return out_df

def grid_pt_sl(pt,sl,close,enter,max_holding,side):
    """
    :param pt: list of profit taking target rate
    :param sl: list of stop loss target rate
    :return: (pd.DataFrame) Cumulative Returns of each pt_sl
            row = profit taking target rate, columns = stop loss target rate
    """
    out = np.ones((len(pt),len(sl)))
    df = pd.DataFrame(out)
    df.index = pt
    df.columns = sl
    for i in pt:
        for j in sl:
            pt_sl = [i,j]
            df.loc[i,j] = get_barrier(close,enter,pt_sl,max_holding,side).ret.cumsum()[-1]
    return df

def get_wallet(close, barrier, initial_money=0, bet_size=None):
    """
    :param close: series of price
    :param barrier: DataFrame from get_barrier()
                barrier must include column 'exit'
    :return: (pd.DataFrame) Cumulative Returns of each pt_sl
            row = profit taking target rate, columns = stop loss target rate
    """
    close = close.round(2)
    if bet_size is None:
        bet_size = pd.Series(np.ones(len(close)),index=close.index)
    bet_amount = bet_size.loc[barrier.index]
    spend = bet_amount*close.loc[barrier.index]
    receive = pd.Series(close.loc[barrier.exit.dropna()].values, index=barrier.dropna(subset=['exit']).index)*bet_amount
    receive = receive.fillna(0)
    close_exit = pd.Series(receive.loc[barrier.index].values,index=barrier.exit).groupby(by='exit',axis=0).sum()
    close_exit = close_exit.rename('money_receive')
    
    wallet_0 = pd.DataFrame({'exit':barrier.exit,'price':close,'money_spent':spend})
    wallet = wallet_0.join(close_exit).fillna(0)
    wallet = wallet.drop(index= wallet.loc[wallet.money_spent+wallet.money_receive==0].index)
    
    buy_amount = bet_amount
    buy_amount = buy_amount.rename('buy_amount')
    sell_amount = (wallet.money_receive/wallet.price).round()
    sell_amount = sell_amount.rename('sell_amount')
    
    n_stock = ((wallet.money_spent/wallet.price).round()-(wallet.money_receive/wallet.price).round()).cumsum()
    n_stock = n_stock.rename('n_stock')
    
    inventory = (-wallet.money_spent+wallet.money_receive).cumsum() + initial_money
    inventory = inventory.rename('cash_inventory')
    
    out = wallet.join([buy_amount,sell_amount,n_stock,inventory])
    out = out.fillna(0)
    return out

def show_results(wallet):
    """
    

    Parameters
    ----------
    wallet : dataframe from get_wallet()

    Returns
    -------
    show results

    """
    initial_invest = wallet.cash_inventory[0]+wallet.money_spent[0]
    cash_in_hand = wallet.cash_inventory[-1]
    stock_owned = wallet.n_stock[-1]
    stock_price_now = wallet.price[-1]
    total_asset = cash_in_hand + stock_owned*stock_price_now
    total_gain = total_asset-initial_invest
    total_return = total_gain/initial_invest
    tcost = wallet.money_receive.sum() * 0.003 + 0 # 0.3% tax, no fee
    
    print("Your initial investment money : {}".format(initial_invest))
    print("You now have cash : {}".format(cash_in_hand))
    print("You now have n of stocks : {}".format(stock_owned))
    print("Your total asset (cash+stock) now : {}".format(total_asset))
    print("Total gain : {}".format(total_gain))
    print("Transaction costs : {}".format(tcost))
    print("Total profit : {}".format(total_gain-tcost))

def get_plot_wallet(close,barrier,wallet):
    
    plot_df = close.to_frame().join(barrier)
    ret_abs = plot_df.ret.abs()
    plot_df['ret_size']=ret_abs
    ret_sign = np.sign(plot_df.ret)
    dfret = ret_sign.to_frame()
    dfret[dfret.ret==1] = 'profit'
    dfret[dfret.ret==-1] = 'loss'
    dfret[dfret.ret==0] = 'exit point'
    plot_df['This bet is']=dfret.ret
    plot_wallet = wallet.join(plot_df.dropna()[['This bet is','ret_size']])
    plot_wallet = plot_wallet.reset_index()
    plot_wallet = plot_wallet.fillna({'This bet is':'exit point','ret_size':0})
    plot_wallet = plot_wallet.rename(columns={'timestamp':'Date'})
    return plot_wallet

def get_metalabel(barrier):
    
    """
    Parameters
    ----------
    barrier : dataframe
        from get_barrier()

    Returns
    -------
    series of meta-label (1 profit(go) 0 loss(pass))

    """
    retsign = np.sign(barrier.ret)
    retsign = retsign.loc[retsign!=0]
    out = .5*(retsign+1)
    out = out.rename('label')
    return out

def plot(close,barrier,wallet):   
    plot_wallet = get_plot_wallet(close,barrier,wallet)
    initial_invest = wallet.cash_inventory[0]+wallet.money_spent[0]
    cash_in_hand = wallet.cash_inventory[-1]
    stock_owned = wallet.n_stock[-1]
    stock_price_now = wallet.price[-1]
    total_asset = cash_in_hand + stock_owned*stock_price_now
    total_gain = total_asset-initial_invest
    total_return = total_gain/initial_invest
    
    fig = px.scatter(plot_wallet, x="Date", y="price", size='buy_amount', color='This bet is'
                     ,size_max=10, hover_data=['exit','n_stock','cash_inventory','money_spent','money_receive'],color_discrete_sequence=["red", "black", "blue"])
    
    fig.update_xaxes(ticklabelmode="period")
    fig.update_layout(title_text='Now having cash + stock value = {}, Total gain = {}'.format(total_asset.round(2),(total_gain).round(2)))
    fig.add_trace(go.Scatter(x=close.index, y=close, mode='lines', name="Close Price",opacity=0.4))
    
    fig.show()

