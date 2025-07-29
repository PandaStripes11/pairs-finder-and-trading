import pandas as pd
from data import fetch_data
from utils.plot_results import *

def calculate_zscore(spread):
    mean = spread.rolling(window=30).mean()
    std = spread.rolling(window=30).std()
    zscore = (spread - mean) / std
    return zscore

def generate_signals(zscore, entry_threshold=1.0, exit_threshold=0.0):
    signals = pd.Series(index=zscore.index, data=0)
    long = zscore < -entry_threshold
    short = zscore > entry_threshold
    exit = abs(zscore) < exit_threshold
    
    position = 0
    for i in range(len(zscore)):
        if long[i]:
            position = 1
        elif short[i]:
            position = -1
        elif exit[i]:
            position = 0
        signals[i] = position
    return signals

def backtest(df, signals, correlation = 1):
    returns = df.pct_change().dropna()
    position = signals.shift().fillna(0)

    pnl = correlation * position * (returns.iloc[:, 0] - returns.iloc[:, 1])
    cum_pnl = pnl.cumsum()

    return cum_pnl, pnl

def trade_pair():
    stock_ticker1 = input("Enter first stock symbol --> ")
    stock_ticker2 = input("Enter second stock symbol --> ")
    df = fetch_data.fetch_pair_data(stock_ticker1, stock_ticker2)
    df.to_csv("data/raw-data.csv")

    spread = df[stock_ticker1] - df[stock_ticker2]
    correlation = df[stock_ticker1].corr(df[stock_ticker2])
    zscore = calculate_zscore(spread)
    signals = generate_signals(zscore)
    cum_pnl, pnl = backtest(df, signals, correlation=np.sign(correlation))
    plot_results(cum_pnl, zscore, signals)