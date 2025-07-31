import React from "react";

export function HeroBanner() {
  return (
    <section className="hero-banner">
      {/* Top decorative wave */}
      <svg
        className="hero-wave-top"
        viewBox="0 0 1440 320"
        preserveAspectRatio="none"
      >
        <path
          fill="#A56EFF"
          fillOpacity="0.25"
          d="M0,96L40,122.7C80,149,160,203,240,218.7C320,235,400,213,480,202.7C560,192,640,192,720,181.3C800,171,880,149,960,133.3C1040,117,1120,107,1200,106.7C1280,107,1360,117,1400,122.7L1440,128L1440,0L1400,0C1360,0,1280,0,1200,0C1120,0,1040,0,960,0C880,0,800,0,720,0C640,0,560,0,480,0C400,0,320,0,240,0C160,0,80,0,40,0L0,0Z"
        />
      </svg>

      <div className="hero-content">
        <h1 className="hero-title">Pairs Trading Visualizer</h1>
        <p className="hero-description">
          Explore stock relationships with correlation heatmaps, backtest
          strategies, and gain trading insights.{" "}
          <strong>Find a stock pair to trade.</strong>
        </p>
      </div>

      {/* Bottom decorative wave */}
      <svg
        className="hero-wave-bottom"
        viewBox="0 0 1440 320"
        preserveAspectRatio="none"
      >
        <path
          fill="#F78AFF"
          fillOpacity="0.2"
          d="M0,160L48,149.3C96,139,192,117,288,122.7C384,128,480,160,576,176C672,192,768,192,864,186.7C960,181,1056,171,1152,149.3C1248,128,1344,96,1392,80L1440,64L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"
        />
      </svg>
    </section>
  );
}
