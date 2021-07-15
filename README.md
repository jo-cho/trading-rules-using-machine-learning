# High-Frequency Trading rules using machine learning 


- This is my financial trading system using ML.

- See [Notebook](ETCUSD-trading-ML.ipynb)

- I'm still working on this project. If you're interested, feel free to contact me.

Version 2.0

Momentum strategy + Meta-Labeling

1. [Financial Data and Bars](#financial-data-and-bars)

    - [OHLCV Bars](#ohlcv-bars)
    - [Summary and plot](#summary-and-plot)

2. Getting Trend Signals (Long only)
    -

3. Labeling with Triple-Barrier Method
    - Form Symmetric Triple Barrier with signals
    - Binary Labeling (Profit or Loss)


4. Secondary Model

- Features (X)
    - Market/ Microstructure features/ Fundamentals/ Sentiments/
    - Feature Scaling (MinMaxScaler)
    - Feature Engineering (PCA/ Autoencoder)
    
- Prediction Model
    - Simple Split
    - AutoML with autogluon and select the best model
    - Results
    
- Trading
    - Bet Sizing
 
5. Results
    - Cumulative returns, Sharpe Ratio, Drawdown

## Financial Data and Bars

 - ETH/USD 5 min data (2019.1.1 ~ now)
 - The trading rule is based on Triple-Barrier Method introduced in Lopez De Prado (2018).


# References: 
- Advances in Financial Machine Learning, Lopez de Prado (2018)
- *ta*, https://github.com/bukosabino/ta

