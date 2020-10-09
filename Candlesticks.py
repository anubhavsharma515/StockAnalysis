from alpha_vantage.timeseries import TimeSeries
from mpl_finance import candlestick_ohlc
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
from GetDate import get_dates
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

matplotlib.use('TkAgg')


def candle_stick(symbol, date_option,root):
    symbol = symbol.get()
    ts = TimeSeries(key = 'GKLUSRM3E6Y6548B', output_format = 'pandas')
    stock, metadata = ts.get_daily_adjusted(symbol, outputsize = 'full')
    stock = stock.sort_index(axis = 0, ascending = True)
    time = get_dates(date_option)
    stock.drop(['7. dividend amount', '8. split coefficient'], axis=1,inplace= True)
    stock.columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    stock.to_csv(f"{symbol}.csv")
    stock_csv = pd.read_csv(f"{symbol}.csv", parse_dates= True, index_col=0)
    if time == (20*253):
        print(time)
        graph = Tk()
        graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))

        graph.title(f"{symbol} CandleStick {time} Years")
        stock_ohlc = stock_csv['Adj Close'].resample('10D').ohlc()
        stock_volume = stock_csv['Volume'].resample('10D').sum()
        stock_ohlc.reset_index(inplace = True)
        stock_ohlc['date'] = stock_ohlc['date'].map(mdates.date2num)
        fig  = plt.Figure(figsize = (5,4), dpi=100)
        ax1 = fig.add_subplot(111)
        candlestick_ohlc(ax1, stock_ohlc.values, colorup = 'g')
        ax1.xaxis_date()
        canvas = FigureCanvasTkAgg(fig, graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand =1)
        toolbar = NavigationToolbar2Tk(canvas, graph)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand =1)
        Back_Button = Button(graph, text = "Go Back", command = lambda: raise_frame(root, graph)).pack()
    else:
        partial_data(stock_csv, time, symbol,root)
    return

def raise_frame(frame, current):
    frame.tkraise()
    current.destroy()

def partial_data(stock_csv, time,symbol,root):
    graph = Tk()
    graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))
    graph.title(f"{symbol} CandleStick {time} Years")
    stock_csv = stock_csv[:time]
    stock_ohlc = stock_csv['Adj Close'].resample('10D').ohlc()
    stock_volume = stock_csv['Volume'].resample('10D').sum()
    stock_ohlc.reset_index(inplace = True)
    stock_ohlc['date'] = stock_ohlc['date'].map(mdates.date2num)
    fig  = plt.Figure(figsize = (5,4), dpi=100)
    ax1 = fig.add_subplot(111)
    candlestick_ohlc(ax1, stock_ohlc.values, colorup = 'g')
    ax1.xaxis_date()
    canvas = FigureCanvasTkAgg(fig, graph)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand =1)
    toolbar = NavigationToolbar2Tk(canvas, graph)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand =1)
    Back_Button = Button(graph, text = "Go Back", command = lambda: raise_frame(root, graph)).pack()
       








    
