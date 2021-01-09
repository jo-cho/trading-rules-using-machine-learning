# Trading rules using machine learning 
## by jojothepizza
Version 1.6.

- This is my financial trading system using ML.

- I'm still working on this project. If you're interested, feel free to contact me.

# Results
 - This is the results of my trading strategies (there's full code in *Notebooks*).
 - The trading rule is based on Triple-Barrier Method introduced in Lopez De Prado (2018).
 - Here are Annualized Sharpe Ratio and Cumulative Returns of three strategies (only long strategy which excludes short selling):
 1. Trading Strategy: This is a *primary model* using only technical analysis. (predict when to buy)
 2. Meta-Label: This is a *secondary model* using ML algorithm on the trading strategy. (predict whether its bet is profit or loss/ correct bets of the trading strategy) /I used Random Forest here.
 3. Bet Sizing: This is a *sizing model* using predict probabilities of ML algorithm used in Meta-Labeling (decide how much to buy)
 4. Buy and hold: Buy-and-hold for an entire period.
 
 And those strategies were introduced in *Lopez de Prado*, **Advances in Financial Machine Learning**.
 
### BTC-USD (30 minutes data)
![BTCUSD Annualized Sharpe Ratio](https://user-images.githubusercontent.com/52461409/104087088-9b60f600-52a0-11eb-8647-d3426ddabd39.png)
![BTCUSD cumret](https://user-images.githubusercontent.com/52461409/104087089-9c922300-52a0-11eb-979b-d9c2ad10999d.jpg)

### Samsung Electronics (Daily data)
![SE Annualized Sharpe Ratio](https://user-images.githubusercontent.com/52461409/104087185-3a85ed80-52a1-11eb-8a56-6ed015e78327.png)
![SE cumret](https://user-images.githubusercontent.com/52461409/104087186-3b1e8400-52a1-11eb-9220-c48857479baa.jpg)

### SK Hynix (Daily data)
![SK하이닉스 Annualized Sharpe Ratio](https://user-images.githubusercontent.com/52461409/104093517-4cca5080-52ce-11eb-9b10-17220d3b430c.png)
![SK하이닉스 cumret](https://user-images.githubusercontent.com/52461409/104093518-4cca5080-52ce-11eb-8662-74bfa3550dc1.jpg)

### LG Chemicals (Daily data)
![LG화학 Annualized Sharpe Ratio](https://user-images.githubusercontent.com/52461409/104093513-4c31ba00-52ce-11eb-8ea2-27f90df14e2b.png)
![LG화학 cumret](https://user-images.githubusercontent.com/52461409/104093515-4c31ba00-52ce-11eb-8987-7828f92d2484.jpg)

### Hyundai Cars (Daily data)
![현대차 Annualized Sharpe Ratio](https://user-images.githubusercontent.com/52461409/104093511-4b992380-52ce-11eb-94e0-ff0ee820cc45.png)
![현대차 cumret](https://user-images.githubusercontent.com/52461409/104093512-4b992380-52ce-11eb-897d-1d1f26087767.jpg)

### Naver (Daily data)
![네이버 Annualized Sharpe Ratio](https://user-images.githubusercontent.com/52461409/104093508-49cf6000-52ce-11eb-8e01-9365a1529d3c.png)
![네이버 cumret](https://user-images.githubusercontent.com/52461409/104093510-4b008d00-52ce-11eb-84c2-426179f75a7a.jpg)

Huge thanks to Lopez de Prado and a python libary *mlfinlab*
