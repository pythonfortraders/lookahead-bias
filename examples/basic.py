"""
This script demonstrates the concept of lookahead bias in trading strategies.

Lookahead bias is when we use future information to make current decisions.
This is easy to do when we are looking at historical data, but leads to strategies
we can't trade in the real world.

This code is the simplest and most pathological example of lookahead bias: it uses
tomorrow's return to make today's trading decision. The crystal ball strategy!
"""

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical price data for AAPL
data = yf.download("AAPL", start="2024-01-01", end="2024-11-18", progress=False)


# Create a strategy that goes long if the next day's return is positive
# The shift(-1) brings the next day's return to the current day, creating lookahead bias!
def make_strategy(data):
    data["Next_Return"] = data["Adj Close"].pct_change().shift(-1)
    data["Signal"] = np.where(data["Next_Return"] > 0, 1, -1)  # Make long/short signal
    data["Daily_Return"] = data["Signal"] * data["Next_Return"]
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


data = make_strategy(data)
plot_backtest(data, "Strategy Backtest")
