import React, { useState } from "react";

export function AssetInput({ onSubmit }) {
  const [input, setInput] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    let tickers = input.split(",").map((t) => t.trim().toUpperCase());
    if (tickers.length > 20) {
      tickers = tickers.slice(0, 20);
    }
    onSubmit(tickers);
  };

  return (
    <form onSubmit={handleSubmit} className="asset-form">
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter comma-separated tickers (e.g. KO, PEP, MCD)"
        className="asset-input"
      />
      <button type="submit" className="submit-button">
        Generate Heatmaps
      </button>
    </form>
  );
}
