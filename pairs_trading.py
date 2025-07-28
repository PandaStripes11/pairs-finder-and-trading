from backtest import *
from plot_results import *
from data import fetch_data

if __name__ == "__main__":
    df = fetch_data.fetch_pair_data("KO", "PEP")
    df.to_csv("data/raw-data.csv")

    spread = df["KO"] - df["PEP"]
    zscore = calculate_zscore(spread)
    signals = generate_signals(zscore)
    cum_pnl, pnl = backtest(df, signals)
    plot_results(cum_pnl, zscore, signals)