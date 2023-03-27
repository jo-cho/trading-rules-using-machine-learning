# Trading rules using machine learning 
This is my financial trading using ML.


- [Example](https://github.com/jo-cho/trading-rules-using-machine-learning/blob/main/Notebooks/ETHUSD%20trading%20ML.ipynb)
- [Project](https://github.com/jo-cho/trading-rules-using-machine-learning/tree/main/Notebooks/project)


Momentum prediction and enhancing the strategy with machine learning

1. Financial Data and Bars
    - Form time/dollar bars with tick data

2. Get Buy/Sell Signals
    - Momentum strategy (RSI..)
    - Additional ML regime detector

3. Trading Rules
    - Set enter rules with trading signals from classifiers
    - Set exit rules with profit-taking, stop-loss rate, and maximum holding period
    - (For enhancing the strategy) Label the binary outcome (Profit or Loss)


4. Strategy-Enhancing ML Model

- Get Features (X)

    - Market data & Technical analysis
    - Microstructure features
    - Macroeconomic variables
    - Fundamentals
    - *news/public sentiments* (in progress)

- Feature Engineering
    - Feature selection, dimension reduction
    
- Machine Learning Model Optmization
    - Cross-validation (time-series cv / Purged k-fold)  
    - Hyperparameter tuning
    - AutoML with autogluon (or simply using ensemble methods such as Random forest, LightGBM, or XGBoost)
    - Metrics (accuracy, f1 score, roc-auc)
    
- Outcome
    - Bet confidence (probability to accept a single trading signal)
    
4. Trading Decision
    - Decide to bet or pass for each trading signal from the momentum strategy. The ML model above will help you.
    - Bet sizing with some advanced models (in progress)
    
5. Backtesting
    - Cumulative returns, Sharpe ratio, max drawdown, win ratio


# References: 
- Advances in Financial Machine Learning, Lopez de Prado (2018)

# Flowchart
![ML Trade Networks](https://user-images.githubusercontent.com/52461409/132567663-eeead1ab-d3de-4cf3-a79f-6fea94722999.png)
