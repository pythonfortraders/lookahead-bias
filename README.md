# Lookahead Bias Examples

The most profitable way to trade is owning a time machine or crystal ball. 

If you're not careful with your backtests, you might convince yourself you have one!

Lookahead bias happens when your backtest uses future information to make today's decisions. 
This makes your strategy look amazing, but impossible to achieve in live trading.
It's like taking a practice test by reading off the answer key, then getting an F on the real exam. 

Here are some ways it happens:

* **Shifting Errors**: Time series misalignment issues can leak future info into your strategy. The simplest case would be looking at tomorrow's data today. This sounds like an obvious mistake, but it can creep into your code in subtle ways.

* **Time of Day**: If your strategy uses close prices to calculate its signal, but you place trades at market open. This has lookahead bias because you won't know the close price until the next day!
  
* **Corporate Adjustments**: Events like stock splits, dividends, mergers, and index inclusions can leak future information into past price series when adjusted. 

You can see the drastic difference in the charts below. Often, when a chart looks fantastic, pure up-and-to-the-right, that's a dead ringer for lookahead bias. 

This repository has 2 code examples demonstrating lookahead bias. 

The first ([basic.py](https://github.com/pythonfortraders/lookahead-bias/blob/master/examples/basic.py)) is simple and pathological: it uses tomorrow's returns to pick today's positions.

![bias_basic](https://github.com/pythonfortraders/lookahead-bias/blob/master/plots/bias_basic.png)

The second ([close_minus_open.py](https://github.com/pythonfortraders/lookahead-bias/blob/master/examples/close_minus_open.py)) is more subtle, using a time of day error where it uses close prices to make trades at market open.

![bias_subtle](https://github.com/pythonfortraders/lookahead-bias/blob/master/plots/close_minus_open_biased.png)
![bias_subtle_fixed](https://github.com/pythonfortraders/lookahead-bias/blob/master/plots/close_minus_open_no_bias.png)

More resources on backtesting in Python are available in our [free algorithmic trading community](https://skool.com/algos)!
