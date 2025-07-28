import requests
import pandas as pd
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL

HEADERS = {
    "APCA-API-KEY-ID": ALPACA_API_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY
}

def get_bars(symbol, start, end, timeframe="1Day"):
    url = f"{ALPACA_BASE_URL}/stocks/{symbol}/bars"
    params = {
        "start": start,
        "end": end,
        "timeframe": timeframe,
        "adjustment": "raw",  # or "split", "dividend", etc.
        "limit": 1000
    }
    response = requests.get(url, headers=HEADERS, params=params)
    data = response.json()
    
    if "bars" not in data:
        raise Exception(f"No bars returned for {symbol}: {data}")

    df = pd.DataFrame(data["bars"])
    df["t"] = pd.to_datetime(df["t"])
    df.set_index("t", inplace=True)
    return df["c"]  # Return the closing prices only

def fetch_pair_data(ticker1, ticker2, start="2023-01-01", end="2024-01-01"):
    series1 = get_bars(ticker1, start, end)
    series2 = get_bars(ticker2, start, end)
    df = pd.DataFrame({ticker1: series1, ticker2: series2}).dropna()
    return df

if __name__ == "__main__":
    df = fetch_pair_data("KO", "PEP")
    df.to_csv("data/raw_data.csv")
    print(df.head())