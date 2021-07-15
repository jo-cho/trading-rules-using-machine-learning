# -*- coding: utf-8 -*-
"""
Signals
"""
import numpy as np
import pandas as pd
import ta

def rsi(close,window=14):
        diff = close.diff(1)
        up_direction = diff.where(diff > 0, 0.0)
        down_direction = -diff.where(diff < 0, 0.0)
        emaup = up_direction.ewm(window, adjust=False).mean()
        emadn = down_direction.abs().ewm(window, adjust=False).mean()
        rs = emaup / emadn
        rsi = pd.Series(np.where(emadn == 0, 100, 100 - (100 / (1 + rs))),
                        index=close.index)
        return pd.Series(rsi, name="rsi")

def get_signal_1(close,n1=10,n2=14):
        one = np.sign((close-close.shift(1)).ewm(n1).mean())
        two = np.sign(rsi(close,n2)-50)
        choindex = one+two
        signal = pd.Series(np.where(choindex.shift(1)==2, 1, 0),index=close.index)
        return signal
    
def get_signal_2(close,n1=10,n2=14):
     one = np.sign((close-close.shift(1)).ewm(n1).mean())
     two = np.sign(rsi(close,n2)-58)
     choindex = one+two
     signal = pd.Series(np.where(choindex.shift(1)==2, 1, 0),index=close.index)
     return signal
 
def sma_crossover_signal(close,fast_window,slow_window):
    sma_crossover = pd.DataFrame(close)
    sma_crossover['fast'] = close.rolling(fast_window).mean()
    sma_crossover['slow'] = close.rolling(slow_window).mean()
    sma_crossover.dropna(inplace=True)
    sma_crossover['madiff'] = np.where(sma_crossover.fast>sma_crossover.slow, 1, 0)
    sma_crossover['signal'] = sma_crossover.madiff.diff()
    signal = sma_crossover.signal
    return signal

def rsi_signal(close,window=14,threshold=30):
    rsi_df = pd.DataFrame(rsi(close,window))
    rsi_df['turn'] = np.where(rsi_df.rsi<threshold,-1,0)
    rsi_signal = rsi_df.turn.diff()
    return rsi_signal

def bb_signal(close,n=20):
    bbsignal = pd.DataFrame(close)
    bbsignal['bbbelow'] = np.where(ta.volatility.bollinger_lband(close,n)>close,-1,0)
    signal = bbsignal.bbbelow.diff().dropna()
    return signal