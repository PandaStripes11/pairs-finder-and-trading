// App structure for a React frontend UI to visualize correlation/cointegration heatmaps
// and allow backtesting + plotting of a chosen stock pair.

// File: src/App.jsx
import React, { useState } from "react";
import { AssetInput } from "./components/AssetInput";
import { HeatmapDisplay } from "./components/HeatmapDisplay";
import { PairDetails } from "./components/PairDetails";
import "./App.css";

export default function App() {
  const [assets, setAssets] = useState(["KO", "PEP", "MCD"]);
  const [heatmaps, setHeatmaps] = useState(null);
  const [selectedPair, setSelectedPair] = useState(null);

  const handleHeatmapGeneration = async (tickers) => {
    setAssets(tickers);
    const res = await fetch(
      `http://localhost:8000/heatmaps/?tickers=${tickers.join(",")}`
    );
    const data = await res.json();
    setHeatmaps(data);
  };

  return (
    <div className="app">
      <h1 className="title">Pairs Trading Analyzer</h1>
      <AssetInput onSubmit={handleHeatmapGeneration} />
      {heatmaps && (
        <HeatmapDisplay
          data={heatmaps}
          onPairSelect={(pair) => setSelectedPair(pair)}
        />
      )}
      {selectedPair && <PairDetails pair={selectedPair} />}
    </div>
  );
}
