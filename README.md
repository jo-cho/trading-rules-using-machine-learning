# High-Frequency Trading rules using machine learning 


- This is my financial trading system using ML.

- See [Notebook](https://github.com/jo-cho/trading-rules-using-machine-learning/blob/main/Notebooks/ETHUSD%20trading%20ML.ipynb)

- I'm still working on this project.

Version 2.0

Momentum strategy with machine learning

1. [Financial Data and Bars](#financial-data-and-bars)

    - Form time/dollar bars with tick data

2. Getting Trading Signals
    - Momentum strategy (RSI..)
    - Additional ML regime detector

3. Trading Rules
    - Enter rules with trading signals
    - Exit rules (triple-barrier method)
    - Binary Labeling (Profit or Loss)


4. Strategy Enhancing ML Model

- Get Features (X)

    - Market data & Technical analysis
    - *Microstructure features*
    - *Macroeconomic variables*
    - *Fundamentals*
    - *public sentiments with NLP*

- Feature Engineering
    - Feature scaling
    - Dimension reduction
    - Feature Analysis with feature importance
    - Feature selection
    
- Machine Learning Model
    - Cross-validation (time-series cv / Purged k-fold)  
    - Hyperparameter tuning
    - AutoML with autogluon and select the best model
    - Results (accuracy, f1 score, roc-auc)
    
4. Trading
    - Bet Sizing
    - *Trading Simulation*
    - 
5. Results
    - *Cumulative returns, Sharpe Ratio, max drawdown*

## Financial Data and Bars

 - ETH/USD 5 min data (2019.1.1 ~ now)
 - The trading rule is based on Triple-Barrier Method introduced in Lopez De Prado (2018).


# References: 
- Advances in Financial Machine Learning, Lopez de Prado (2018)
- *ta*, https://github.com/bukosabino/ta
- *autogluon*, https://github.com/awslabs/autogluon

# Flowchart
![ML Trade Networks](https://user-images.githubusercontent.com/52461409/132567663-eeead1ab-d3de-4cf3-a79f-6fea94722999.png)
