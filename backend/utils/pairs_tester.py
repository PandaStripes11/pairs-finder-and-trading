import itertools
from statsmodels.tsa.stattools import coint
import pandas as pd
import numpy as np
from datetime import date, timedelta
from data.fetch_data import fetch_multiple_data  # You may need to implement this

yesterday_date = date.today() - timedelta(days=1)
def find_cointegrated_pairs(tickers: list, start="2023-01-01", end=(yesterday_date.strftime("%Y-%m-%d")), timeframe="1D", min_corr=0.9, max_pval=0.05):
    df = fetch_multiple_data(tickers, start=start, end=end)
    
    # Drop rows with any NaNs
    df = df.dropna()

    results = []

    for (t1, t2) in itertools.combinations(tickers, 2):
        s1 = df[t1]
        s2 = df[t2]
        
        # Calculate correlation
        corr = s1.corr(s2)
        if corr < min_corr:
            continue

        # Calculate cointegration
        stat, pval, _ = coint(s1, s2)
        if pval < max_pval:
            results.append({
                'pair': (t1, t2),
                'correlation': corr,
                'cointegration_pval': pval
            })

    return pd.DataFrame(results).sort_values('cointegration_pval')

def compute_correlation_matrix(tickers: list, start="2023-01-01", end=(yesterday_date.strftime("%Y-%m-%d"))):
    df = fetch_multiple_data(tickers, start=start, end=end).dropna()

    corr_matrix = pd.DataFrame(index=df.columns, columns=df.columns, dtype=float)

    for t1, t2 in itertools.combinations(df.columns, 2):
        corr = df[t1].corr(df[t2])
        corr_matrix.loc[t1, t2] = corr
        corr_matrix.loc[t2, t1] = corr
    
    np.fill_diagonal(corr_matrix.values, 1)
    return corr_matrix

def compute_cointegration_matrix(tickers: list, start="2023-01-01", end=(yesterday_date.strftime("%Y-%m-%d"))):
    df = fetch_multiple_data(tickers, start=start, end=end).dropna()

    pval_matrix = pd.DataFrame(index=df.columns, columns=df.columns, dtype=float)

    for t1, t2 in itertools.combinations(df.columns, 2):
        stat, pval, _ = coint(df[t1], df[t2])

        pval_matrix.loc[t1, t2] = pval
        pval_matrix.loc[t2, t1] = pval
    
    np.fill_diagonal(pval_matrix.values, np.nan)
    return pval_matrix