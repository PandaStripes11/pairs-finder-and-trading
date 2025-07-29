from utils.backtest import *
from utils.plot_results import *
from utils.pairs_tester import *
from data import fetch_data

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

def plot_correlation(tickers: list):
    correlation_matrix = compute_correlation_matrix(tickers[:40])
    plot_heatmap(correlation_matrix, "Correlation matrix for 100 stocks")

def plot_cointegration(tickers: list):
    cointegration_matrix = compute_cointegration_matrix(tickers[:40])
    plot_heatmap(cointegration_matrix, "Cointegration p-values for 100 stocks")

if __name__ == "__main__":
    tickers = [
        "AAPL", "MSFT", "GOOGL", "META", "V", "MA", "JPM", "BAC", "XOM", "CVX",
        "KO", "PEP", "WMT", "TGT", "COST", "BJ", "NVDA", "AMD", "UNH", "HUM",
        "HD", "LOW", "DIS", "PARA", "PYPL", "SQ", "F", "GM", "UAL", "DAL",
        "NKE", "UAA", "GS", "MS", "LUV", "JBLU", "QCOM", "AVGO", "T", "VZ",
        "ABT", "MDT", "BMY", "PFE", "EBAY", "ETSY", "DD", "DOW", "RTX", "LMT",
        "SO", "DUK", "INTC", "MU", "MMM", "HON", "SBUX", "MCD", "CRM", "NOW",
        "CSX", "NSC", "WFC", "USB", "TGT", "DG", "AMZN", "SHOP", "BIGC", "SPGI",
        "MCO", "ADBE", "ANSS", "ROKU", "NFLX", "PLD", "PLD", "AAL", "MAR", "HLT",
        "C", "ABBV", "MRK", "Z", "RDFN", "TDOC", "AMWL", "TSLA", "NIO", "BP",
        "SHEL", "CI", "CNC", "FDX", "UPS", "CHRW", "EXPD"
    ]

    continue_pairs_trade = True
    while continue_pairs_trade:
        trade_pair()
        user_response = input("Continue trading pairs? (Y/N) ")
        continue_pairs_trade = True if user_response == "Y" else False