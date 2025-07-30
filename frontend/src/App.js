// App structure for a React frontend UI to visualize correlation/cointegration heatmaps
// and allow backtesting + plotting of a chosen stock pair.

import React, { useState, useEffect } from "react";
import { AssetInput } from "./components/AssetInput";
import { HeatmapDisplay } from "./components/HeatmapDisplay";
import { PairDetails } from "./components/PairDetails";
import "./App.css";
import LoadingSpinner from "./components/LoadingSpinner";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [assets, setAssets] = useState(["KO", "PEP", "MCD"]);
  const [heatmaps, setHeatmaps] = useState(null);
  const [selectedPair, setSelectedPair] = useState(null);
  const BASE_URL = process.env.REACT_APP_BACKEND_API_BASE_URL;

  const handleHeatmapGeneration = async (tickers) => {
    setLoading(true);
    setAssets(tickers);
    const res = await fetch(
      `${BASE_URL}/heatmaps?tickers=${tickers.join(",")}`
    );
    const data = await res.json();
    setHeatmaps(data);
    setLoading(false);
  };

  return (
    <div className="app">
      <h1 className="title">Pairs Trading Analyzer</h1>
      <AssetInput onSubmit={handleHeatmapGeneration} />
      {loading ? (
        <LoadingSpinner />
      ) : (
        heatmaps && (
          <HeatmapDisplay
            assets={assets}
            data={heatmaps}
            onPairSelect={(pair) => setSelectedPair(pair)}
          />
        )
      )}
      {selectedPair && <PairDetails pair={selectedPair} />}
    </div>
  );
}
