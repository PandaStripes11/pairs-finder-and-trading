import React, { useState, useMemo, useEffect } from "react";
import Plot from "react-plotly.js";

export function HeatmapDisplay({ assets, data, onPairSelect }) {
  const [revision, setRevision] = useState(0);

  const handlePairClick = (ticker1, ticker2) => {
    if (ticker1 === ticker2) {
      return;
    }
    onPairSelect([ticker1, ticker2]);
  };

  useEffect(() => {
    setRevision((prev) => prev + 1);
  }, [assets, data]);

  const colorscale = [
    [0.0, "#3b0764"], // Deep purple
    [0.25, "#9333ea"], // Violet
    [0.5, "#d946ef"], // Light purple
    [0.75, "#f472b6"], // Soft pink
    [1.0, "#dddddd"], // White glow
  ];

  const heatmapLayout = {
    font: { color: "white" },
    plot_bgcolor: "#121212",
    paper_bgcolor: "#121212",
    xaxis: {
      tickfont: { color: "white" },
      tickangle: 45,
      showgrid: false,
    },
    yaxis: {
      tickfont: { color: "white" },
      showgrid: false,
    },
    margin: { l: 80, r: 20, b: 80, t: 20 },
  };
  let heatmapCorrLayout = heatmapLayout;
  heatmapCorrLayout.title = "Correlation Heatmap";
  let heatmapCoinLayout = heatmapLayout;
  heatmapCoinLayout.title = "Cointegration Heatmap";

  return (
    <div className="heatmap-container">
      <h2>Correlation</h2>
      <Plot
        data={[
          {
            z: data.corrMatrix,
            x: assets,
            y: assets,
            type: "heatmap",
            colorscale: colorscale,
            text: data.corrMatrix.map((row) =>
              row.map((val) => val.toFixed(2))
            ),
            texttemplate: "%{text}",
            hoverongaps: false,
            hovertemplate: "%{y} & %{x}<br>%{z}<extra></extra>", // tooltip content
            showscale: true,
            hoverlabel: {
              font: { color: "white" },
              bgcolor: "#1f2937",
              bordercolor: "#9333ea",
            },
          },
        ]}
        layout={heatmapCorrLayout}
        onClick={(event) => {
          const point = event.points[0];
          const xTicker = point.x;
          const yTicker = point.y;
          handlePairClick(xTicker, yTicker);
        }}
        revision={revision}
      />

      <h2>Cointegration P-Values</h2>
      <Plot
        data={[
          {
            z: data.coinMatrix,
            x: assets,
            y: assets,
            type: "heatmap",
            colorscale: colorscale,
            text: data.coinMatrix.map((row) =>
              row.map((val) => val.toFixed(2))
            ),
            texttemplate: "%{text}",
            hoverongaps: false,
            hovertemplate: "%{y} & %{x}<br>%{z}<extra></extra>", // tooltip content
            showscale: true,
            hoverlabel: {
              font: { color: "white" },
              bgcolor: "#1f2937",
              bordercolor: "#9333ea",
            },
          },
        ]}
        layout={heatmapCoinLayout}
        onClick={(event) => {
          const point = event.points[0];
          const xTicker = point.x;
          const yTicker = point.y;
          handlePairClick(xTicker, yTicker);
        }}
        revision={revision}
      />

      <p className="note">
        Click any two cells on the heatmap to choose a pair to backtest.
      </p>
    </div>
  );
}
