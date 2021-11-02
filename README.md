# High-Frequency Trading rules using machine learning 


- This is my financial trading system using ML.

- See [Notebook](https://github.com/jo-cho/trading-rules-using-machine-learning/blob/main/Notebooks/ETHUSD%20trading%20ML.ipynb)

- I'm still working on this project.

Version 2.0

Momentum strategy + Meta-Labeling

1. [Financial Data and Bars](#financial-data-and-bars)

    - [OHLCV Bars+ Buy volume](#ohlcv-bars)
    - [Summary and plot](#summary-and-plot)

2. Getting Signals
    - Momentum strategy (RSI..)

3. Labeling with Triple-Barrier Method
    - Form Symmetric Triple Barrier with signals
    - Binary Labeling (Profit or Loss)


4. Prediction Model

- Get Features (X)

    - Market data & Technical analysis
    - *Microstructure features*
    - *Fundamentals*
    - *Sentiments with NLP*

- Feature Engineering
    - Feature Scaling (MinMaxScaler)
    - Dimension Reduction (PCA/ Non-Linear Autoencoder)
    
- Machine Learning Model
    - Hyperparameter tuning
    - AutoML with autogluon and select the best model
    - Feature Importance
    - Results with PnL
    
4. Trading
    - Bet Sizing
    - *Trading Simulation*
    - 
5. Results
    - *Cumulative returns, Sharpe Ratio, Drawdown*

## Financial Data and Bars

 - ETH/USD 5 min data (2019.1.1 ~ now)
 - The trading rule is based on Triple-Barrier Method introduced in Lopez De Prado (2018).


# References: 
- Advances in Financial Machine Learning, Lopez de Prado (2018)
- *ta*, https://github.com/bukosabino/ta
- *autogluon*, https://github.com/awslabs/autogluon

# Flowchart
![ML Trade Networks](https://user-images.githubusercontent.com/52461409/132567663-eeead1ab-d3de-4cf3-a79f-6fea94722999.png)
