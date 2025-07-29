import matplotlib.pyplot as plt
import numpy as np
from data import fetch_data

def plot_results(cum_pnl, zscore, signals):
    fig, ax = plt.subplots(2, 1, figsize=(12, 8))

    ax[0].plot(cum_pnl, label="Cumulative PnL")
    ax[0].set_title("Cumulative Profit & Loss")
    ax[0].legend()

    ax[1].plot(zscore, label="Z-Score")
    ax[1].axhline(1.0, color='red', linestyle='--')
    ax[1].axhline(-1.0, color='green', linestyle='--')
    ax[1].set_title("Z-Score of Spread")
    ax[1].legend()

    plt.tight_layout()
    plt.show()

    fig.savefig("results/plots/PnL.png")

    plt.close()

def plot_assets(tickers: list):
    # Assume you have a DataFrame with aligned prices:
    # e.g., from Alpaca or any source, with columns 'KO' and 'PEP'
    df = fetch_data.fetch_multiple_data(tickers)

    # Normalize and plot both stock price series
    df_norm = df / df.iloc[0]  # Divide each column by its first value

    plt.figure(figsize=(10, 6))
    for index_label in df_norm.columns[1:]:
        plt.plot(df_norm.index, df_norm[index_label], label=f'{index_label} (Normalized)', linewidth=2)

    # Formatting
    plt.title(f"{len(df.index)} Asset Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()# Scatter plot

def plot_heatmap(matrix, title, cmap="coolwarm", annot=True):
    fig, ax = plt.subplots(figsize=(16, 12))
    cax = ax.imshow(matrix, cmap=cmap, interpolation='nearest')

    ax.set_xticks(np.arange(len(matrix.columns)))
    ax.set_yticks(np.arange(len(matrix.index)))
    ax.set_xticklabels(matrix.columns)
    ax.set_yticklabels(matrix.index)

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    for i in range(len(matrix.index)):
        for j in range(len(matrix.columns)):
            value = matrix.iloc[i, j]
            label = f"{value:.2f}" if not np.isnan(value) else ""
            ax.text(j, i, label, ha="center", va="center", color="black")

    ax.set_title(title)
    fig.colorbar(cax)
    plt.tight_layout()
    plt.show()