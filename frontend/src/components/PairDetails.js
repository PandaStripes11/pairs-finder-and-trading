import React, { useEffect, useState } from "react";
import LoadingSpinner from "./LoadingSpinner";

export function PairDetails({ pair }) {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const BASE_URL = process.env.REACT_APP_BACKEND_API_BASE_URL;

  useEffect(() => {
    if (!pair) {
      return;
    }

    const fetchResults = async () => {
      setLoading(true);
      const res = await fetch(`${BASE_URL}/backtest?tickers=${pair.join(",")}`);
      const data = await res.json();
      setResult(data);
      setLoading(false);
    };
    fetchResults();
  }, [pair]);

  return (
    <div className="pair-details">
      <h2>Backtest Results for {pair.join(" & ")}</h2>
      {!loading && result ? (
        <img
          src={`data:image/png;base64,${result["asset-plot"]}`}
          alt="Asset Plot"
          className="asset-plot"
        />
      ) : (
        <LoadingSpinner />
      )}
      {!loading && result ? (
        <img
          src={`data:image/png;base64,${result["pnl-plot"]}`}
          alt="PnL Plot"
          className="pnl-plot"
        />
      ) : (
        <LoadingSpinner />
      )}
    </div>
  );
}
