# Trading rules using machine learning 
## by jojothepizza
Version 1.6, 1.7

- This is my financial trading system using ML.

- I'm still working on this project. If you're interested, feel free to contact me.

# Experiments

 - This is the results of my trading strategies (there's full code in *Notebooks*).
 - The trading rule is based on Triple-Barrier Method introduced in Lopez De Prado (2018).

## Data
- BTC-USD (30 minutes data)
![close_price](https://user-images.githubusercontent.com/52461409/104313915-11bd5c80-551c-11eb-9f23-f8fa73e88ddf.jpg)

## First model 1 (get trend signals and position entries)
### SMA 
- long when 10-days-SMA > 30-days-SMA
![smaf](https://user-images.githubusercontent.com/52461409/104313942-17b33d80-551c-11eb-9238-005598758f1f.jpg)
### Force Index
- long when FI>0
![fi_f](https://user-images.githubusercontent.com/52461409/104313940-171aa700-551c-11eb-856a-e16b03f5753c.jpg)
### RSI
- long when RSI>50
![rsi_f](https://user-images.githubusercontent.com/52461409/104313939-171aa700-551c-11eb-9d69-ddfcc205e603.jpg)

### CUSUM Filter
- detect structural change using cumsum of volatility
- filter out entry points
![cusum](https://user-images.githubusercontent.com/52461409/104313937-16821080-551c-11eb-8eb6-23aab2801d54.jpg)

![return_of_1stmodel](https://user-images.githubusercontent.com/52461409/104313933-15e97a00-551c-11eb-9d41-8cb171c73ce5.jpg)
### Combined filter
![entries](https://user-images.githubusercontent.com/52461409/104313935-16821080-551c-11eb-8e10-d7f3df7ed431.jpg)

## First model 2 (set up target rates of each position and exit of it)
- Triple-Barrier method
#### Results of first model
![return_of_1stmodel](https://user-images.githubusercontent.com/52461409/104313933-15e97a00-551c-11eb-9d41-8cb171c73ce5.jpg)
![cm1](https://user-images.githubusercontent.com/52461409/104313931-15e97a00-551c-11eb-9c1d-6889094fd8bc.jpg)
![metalabel](https://user-images.githubusercontent.com/52461409/104313928-14b84d00-551c-11eb-8ed5-813fa22ab71d.jpg)


## Second model
- It is a model that predicts whether the outcome of each bet is profit or loss.
- It corrects bets of the first trading strategy.
### Features
- Technical indicators and price history
- Use MinMaxizer scaler and PCA
![pcacorr](https://user-images.githubusercontent.com/52461409/104313926-14b84d00-551c-11eb-9daa-be3ce324a086.jpg)

### Random Forest
### Results of second model
![cm2](https://user-images.githubusercontent.com/52461409/104313929-1550e380-551c-11eb-96f1-7414d31ae4fa.jpg)
![cvroc](https://user-images.githubusercontent.com/52461409/104313925-141fb680-551c-11eb-9a0e-e9dcfb0b1852.jpg)
![betpred](https://user-images.githubusercontent.com/52461409/104313924-141fb680-551c-11eb-86c5-549b9be60690.jpg)

## Bet sizing
- Decide how much to buy
- Bet sizing based on Sharpe ratio & Gaussian distribution (Lopez de Prado, 2018)
- Use probabilities of Random forest classification predicted probabilities
- Scale with minmaxizer

![Prob](https://user-images.githubusercontent.com/52461409/104313923-13872000-551c-11eb-856b-ea5d09e924cf.jpg)
![betsize](https://user-images.githubusercontent.com/52461409/104313920-13872000-551c-11eb-9422-ceee79ed5c54.jpg)


## Results
- Here are Annualized Sharpe Ratio and Cumulative Returns of three strategies (only long strategy which excludes short selling):
 1. First trading Strategy: This is a *primary model* using only technical analysis. (predict when to buy)
 2. Second Meta-Label: This is a *secondary model* using ML algorithm on the trading strategy. (predict whether its bet is profit or loss/ correct bets of the trading strategy) /I used Random Forest and LSTM here.
 3. Bet Sizing: This is a *sizing model* using predict probabilities of ML algorithm used in Meta-Labeling ()
 4. Buy and hold: Buy-and-hold for an entire period.
 
 And those strategies were introduced in *Lopez de Prado*, **Advances in Financial Machine Learning**.
 
![BTCUSD Annualized Sharpe Ratio](https://user-images.githubusercontent.com/52461409/104087088-9b60f600-52a0-11eb-8647-d3426ddabd39.png)
![cumret](https://user-images.githubusercontent.com/52461409/104313918-12ee8980-551c-11eb-916a-34c506afa1bf.jpg)



# Other assets results 
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

# With LSTM

### BTC-USD (30 minutes data)
![BTCUSD LSTM Annualized Sharpe Ratio](https://user-images.githubusercontent.com/52461409/104122594-4b119300-5389-11eb-9811-85b725295367.png)
![BTCUSD LSTM cumret](https://user-images.githubusercontent.com/52461409/104122589-4947cf80-5389-11eb-93c4-f754367d6905.jpg)

### Samsung Electronics (Daily data)
![SE LSTM Annualized Sharpe Ratio](https://user-images.githubusercontent.com/52461409/104122591-4a78fc80-5389-11eb-8673-ed6254e9a1ac.png)
![SE LSTM Cumret](https://user-images.githubusercontent.com/52461409/104122592-4a78fc80-5389-11eb-8761-33c07c949286.jpg)


# References: 
- Lopez de Prado (2018) and a python libary *mlfinlab*

