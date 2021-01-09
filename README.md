# Trading rules using machine learning by jojothepizza
Version 1.6.

This is my financial trading system using ML.

I'm still working on this project. If you're interested, feel free to contact me.

# Results
 This is the results of my trading strategies (further explanations in *Notebooks*).
 The trading rule is based on Triple-Barrier Method introduced in Lopez De Prado (2018).
 Here are Annualized Sharpe Ratio and Cumulative Returns of three strategies (only long strategy which excludes short selling):
 1. Trading Strategy: This is a *primary model* using only technical analysis. (predict when to buy)
 2. Meta-Label: This is a *secondary model* using ML algorithm on the trading strategy. (predict its bet is whether profit or loss/ correct the bets of the trading strategy) /I used Random Forest.
 3. Bet Sizing: This is a betting model using predict probabilities of ML algorithm used in Meta-Labeling (decide how much to buy/ maximize Sharpe ratio/ manage risk)
 
 * And those strategies were introduced in *Lopez de Prado*, **Advances in Financial Machine Learning**.
### BTC-USD (30 minutes data)

![BTCUSD Annualized Sharpe Ratio](https://user-images.githubusercontent.com/52461409/104087088-9b60f600-52a0-11eb-8647-d3426ddabd39.png)
![BTCUSD cumret](https://user-images.githubusercontent.com/52461409/104087089-9c922300-52a0-11eb-979b-d9c2ad10999d.jpg)

### Samsung Electronics (Daily data)

![SE Annualized Sharpe Ratio](https://user-images.githubusercontent.com/52461409/104087185-3a85ed80-52a1-11eb-8a56-6ed015e78327.png)
![SE cumret](https://user-images.githubusercontent.com/52461409/104087186-3b1e8400-52a1-11eb-9220-c48857479baa.jpg)

Huge thanks to Lopez de Prado and a python libary *mlfinlab*
