from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from data.fetch_data import fetch_multiple_data
from utils.plot_results import generate_heatmaps
from io import BytesIO
import base64

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/heatmaps/")
def get_heatmaps(tickers: str = Query(...)):
    tickers = tickers.split(",")
    tickers = [ticker.strip() for ticker in tickers]
    corr_img, coin_img = generate_heatmaps(tickers)

    return {
        "correlation": corr_img,
        "cointegration": coin_img
    }