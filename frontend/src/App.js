// App structure for a React frontend UI to visualize correlation/cointegration heatmaps
// and allow backtesting + plotting of a chosen stock pair.

import React, { useState } from "react";
import { HeroBanner } from "./components/HeroBanner";
import { AssetInput } from "./components/AssetInput";
import { HeatmapDisplay } from "./components/HeatmapDisplay";
import { PairDetails } from "./components/PairDetails";
import LoadingSpinner from "./components/LoadingSpinner";
import "./App.css";

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
    <>
      <HeroBanner />
      <svg
        className="hero-wave-border"
        viewBox="0 0 1440 320"
        preserveAspectRatio="none"
      >
        <path
          fill="#F78AFF"
          fillOpacity="0.2"
          d="M0,160L48,149.3C96,139,192,117,288,122.7C384,128,480,160,576,176C672,192,768,192,864,186.7C960,181,1056,171,1152,149.3C1248,128,1344,96,1392,80L1440,64L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"
        />
      </svg>
      <div className="app">
        <h1 className="title">Analyze Stocks</h1>
        <AssetInput onSubmit={handleHeatmapGeneration} />
        {loading ? (
          <LoadingSpinner />
        ) : heatmaps ? (
          <HeatmapDisplay
            assets={assets}
            data={heatmaps}
            onPairSelect={(pair) => setSelectedPair(pair)}
          />
        ) : null}
        {selectedPair && <PairDetails pair={selectedPair} />}
      </div>
    </>
  );
}
