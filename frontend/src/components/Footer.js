import React from "react";

export function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <p>
          <strong>Created by Donte Truong</strong>
        </p>
        <p>
          Contact:{" "}
          <a href="mailto:dontetruong@gmail.com">dontetruong@gmail.com</a>
        </p>
        <p>
          GitHub:{" "}
          <a
            href="https://github.com/PandaStripes11"
            target="_blank"
            rel="noopener noreferrer"
          >
            PandaStripes11
          </a>
        </p>
      </div>
    </footer>
  );
}
