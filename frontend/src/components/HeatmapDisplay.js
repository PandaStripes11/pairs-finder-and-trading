import React from "react";

export function HeatmapDisplay({ data, onPairSelect }) {
  const handlePairClick = (ticker1, ticker2) => {
    onPairSelect([ticker1, ticker2]);
  };

  return (
    <div className="heatmap-container">
      <h2>Correlation</h2>
      <img
        src={`data:image/png;base64,${data.correlation}`}
        alt="Correlation Heatmap"
        className="heatmap"
      />

      <h2>Cointegration P-Values</h2>
      <img
        src={`data:image/png;base64,${data.cointegration}`}
        alt="Cointegration Heatmap"
        className="heatmap"
      />

      <p className="note">
        Click any two cells on the heatmap to choose a pair to backtest.
      </p>
    </div>
  );
}
