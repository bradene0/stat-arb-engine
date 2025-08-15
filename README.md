# Stat-Arb Engine

A Python-based backtesting engine for a classic statistical arbitrage pairs trading strategy. This system identifies pairs of historically related assets and bets on the mean reversion of their price spread.

The core of the strategy is based on finding two cointegrated assets and using a rolling Z-score of their spread to generate trading signals. The engine is designed to be modular and easily configurable for testing different parameters and asset lists.

## Features

-   **Dynamic Hedge Ratio:** Uses a rolling Ordinary Least Squares (OLS) regression to calculate the hedge ratio between pairs, adapting to changing market conditions.
-   **Z-Score Signal Generation:** Calculates a standardized Z-score for the pair's spread to identify statistically significant deviations from the mean.
-   **Configurable Strategy Parameters:** Easily adjust tickers, date ranges, and strategy thresholds (entry/exit Z-scores, rolling windows) in a single `config.py` file.
-   **Volatility Targeting:** Scales positions to target a constant level of daily volatility, leading to a more stable risk profile.
-   **Transaction Cost Simulation:** Includes a simple transaction cost model to provide more realistic performance metrics.
-   **Modular Structure:** The code is logically separated into modules for data loading, signal generation, backtesting, and analysis, making it easy to maintain and extend.

## Project Structure

The repository is organized to separate configuration, source code, and analysis:
