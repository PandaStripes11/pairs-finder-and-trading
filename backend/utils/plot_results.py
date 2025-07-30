import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from data import fetch_data
from utils.pairs_tester import *
import io, base64

# Set the dark theme
mpl.rcParams.update({
    'figure.facecolor': '#121212',        # dark slate
    'axes.facecolor': '#121212',
    'axes.edgecolor': '#7749a3',          # violet
    'axes.labelcolor': '#f472b6',         # pink
    'xtick.color': '#e5e7eb',             # light gray
    'ytick.color': '#e5e7eb',
    'text.color': '#f472b6',
    'axes.titleweight': 'bold',
    'axes.titlecolor': '#d946ef',
    'grid.color': "#7749a3",
    'legend.edgecolor': '#7749a3',
    'legend.facecolor': '#1f2937',
    'legend.fontsize': 'medium',
    'lines.linewidth': 2.5,
    'savefig.facecolor': '#121212',
    'savefig.edgecolor': '#121212',
})
mpl.rcParams['font.family'] = 'DejaVu Sans'

def plot_results(cum_pnl, zscore, signals, show=True):
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
    if show: plt.show()
    else: return fig

def plot_assets(tickers: list, show=True):
    # Assume you have a DataFrame with aligned prices:
    # e.g., from Alpaca or any source, with columns 'KO' and 'PEP'
    df = fetch_data.fetch_multiple_data(tickers)

    # Normalize and plot both stock price series
    df_norm = df / df.iloc[0]  # Divide each column by its first value

    fig = plt.figure(figsize=(10, 6))
    for index_label in df_norm.columns:
        plt.plot(df_norm.index, df_norm[index_label], label=f'{index_label} (Normalized)', linewidth=2)

    # Formatting
    plt.title(f"{len(df.columns)} Asset Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    if show: plt.show() # Scatter plot
    else: return fig

def plot_heatmap(matrix, title, cmap="coolwarm", annot=True, show=True):
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
    if show: 
        plt.show()
    else: 
        return fig

def plot_correlation_heatmap(tickers: list):
    correlation_matrix = compute_correlation_matrix(tickers[:40])
    return plot_heatmap(correlation_matrix, "Correlation matrix for 100 stocks", show=False)

def plot_cointegration_heatmap(tickers: list):
    cointegration_matrix = compute_cointegration_matrix(tickers[:40])
    return plot_heatmap(cointegration_matrix, "Cointegration p-values for 100 stocks", show=False)

# analysis/heatmap.py
def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

def generate_heatmaps(tickers):
    corr_fig = plot_correlation_heatmap(tickers)
    coin_fig = plot_cointegration_heatmap(tickers)

    return fig_to_base64(corr_fig), fig_to_base64(coin_fig)