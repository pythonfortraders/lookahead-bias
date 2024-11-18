"""
Here's a more subtle example of lookahead bias.

This strategy uses close - open as a signal and trades on a daily basis.

The problem?

It enters trades at today's market open, but we don't know the close price until
after the market closes!

To trade this strategy in the real world, we would need to look at yesterday's
close price to make today's trading decision.
"""

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


# Download historical price data for AAPL
data = yf.download("AAPL", start="2024-01-01", end="2024-11-18", progress=False)
data = data.droplevel("Ticker", axis=1)


def make_strategy_with_lookahead_bias(data):
    data = data.copy()
    data["Close_minus_Open"] = data["Close"] - data["Open"]
    data["Signal"] = np.where(data["Close_minus_Open"] > 0, 1, -1)
    data["Daily_Return"] = data["Signal"] * (data["Close"] / data["Open"] - 1)
    data["Cumulative_Return"] = (1 + data["Daily_Return"]).cumprod()
    return data


def make_strategy_without_lookahead_bias(data):
    data = data.copy()
    data["Close_minus_Open"] = data["Close"] - data["Open"]
    data["Signal"] = np.where(data["Close_minus_Open"].shift(1) > 0, 1, -1)
    data["Daily_Return"] = data["Signal"] * (data["Close"] / data["Open"] - 1)
    data["Cumulative_Return"] = (1 + data["Daily_Return"]).cumprod()
    return data


def plot_backtest(data, title):
    data["Cumulative_Return"].plot()
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    data_with_lookahead_bias = make_strategy_with_lookahead_bias(data)
    data_without_lookahead_bias = make_strategy_without_lookahead_bias(data)

    plot_backtest(data_with_lookahead_bias, "Close-Open Strategy with Lookahead Bias")
    plot_backtest(data_without_lookahead_bias, "Close-Open Strategy w/o Lookahead Bias")
