import React, { useEffect, useState } from "react";

export function PairDetails({ pair }) {
  const [result, setResult] = useState(null);

  useEffect(() => {
    const fetchResults = async () => {
      const res = await fetch("http://localhost:8000/api/backtest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pair }),
      });
      const data = await res.json();
      setResult(data);
    };
    fetchResults();
  }, [pair]);

  return (
    <div className="pair-details">
      <h2>Backtest Results for {pair.join(" & ")}</h2>
      {result ? (
        <img
          src={`data:image/png;base64,${result.pnl_plot}`}
          alt="PnL Plot"
          className="pnl-plot"
        />
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}
