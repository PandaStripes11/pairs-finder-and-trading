from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

from utils.plot_results import generate_heatmaps
from utils.pairs_tester import *
from utils.backtest import *

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","https://pairs-trading-analyzer.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/heatmaps")
def get_heatmaps(tickers: str = Query(...)):
    tickers = tickers.split(",")
    tickers = [ticker.strip() for ticker in tickers]
    corr_img, coin_img = generate_heatmaps(tickers)
    corr_matrix, coin_matrix = compute_correlation_matrix(tickers), compute_cointegration_matrix(tickers)
    corr_matrix_cleaned = corr_matrix.replace([np.inf, -np.inf], np.nan).fillna(0)
    coin_matrix_cleaned = coin_matrix.replace([np.inf, -np.inf], np.nan).fillna(0)

    return JSONResponse(content={
        "correlation": corr_img,
        "cointegration": coin_img,
        "corrMatrix": corr_matrix_cleaned.values.tolist(),
        "coinMatrix": coin_matrix_cleaned.values.tolist(),
        "tickers": corr_matrix.columns.tolist()
    })

@app.get("/backtest")
def get_heatmaps(tickers: str = Query(...)):
    tickers = tickers.split(",")
    tickers = [ticker.strip() for ticker in tickers]

    pnl_plot = trade_pair(*tickers, show=False)
    asset_plot = plot_assets(tickers, show=False)

    return JSONResponse(content={
        "pnl-plot": fig_to_base64(pnl_plot),
        "asset-plot": fig_to_base64(asset_plot),
    })

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")