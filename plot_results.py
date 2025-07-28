import matplotlib.pyplot as plt

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