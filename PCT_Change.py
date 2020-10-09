from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
from tkinter import *
import matplotlib.dates as mdates
from GetDate import get_dates as gd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

style.use('ggplot')

def pct_change(symbol, date_option):
    check(symbol)
    time = gd(date_option)
    ts =  TimeSeries(key = 'GKLUSRM3E6Y6548B', output_format= 'pandas')
    ticker, metadata = ts.get_daily_adjusted(symbol, outputsize = 'full')
    ticker = ticker.sort_index(axis=0 ,ascending=True)
    ticker = ticker.drop(['7. dividend amount', '8. split coefficient'], axis=1)
    ticker.columns=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    ticker.to_csv(f"{symbol}.csv")
    ticker_file = pd.read_csv(f"{symbol}.csv", parse_dates = True, index_col= 0)
    ticker_file.reset_index(inplace=True)
    if time==20:
        ticker_file['Pct Change'] = (ticker_file['Adj Close']/ticker_file['Adj Close'].shift(1)) - 1
        plt.plot(ticker_file['date'],ticker_file['Pct Change'])
        plt.show()
    else:
        partial_change(ticker_file, time)
    return

def partial_change(stock_csv, time):
    stock_csv = stock_csv[:time]
    stock_csv['Pct Change'] = (stock_csv['Adj Close']/stock_csv['Adj Close'].shift(1)) - 1
    plt.plot(stock_csv['date'],stock_csv['Pct Change'])
    plt.show()
