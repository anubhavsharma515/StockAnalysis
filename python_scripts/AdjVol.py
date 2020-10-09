from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
from tkinter import *
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk



style.use('ggplot')


def get_ticker_data(symbol,root):
    graph = Tk()
    graph.geometry("{0}x{1}+0+0".format(graph.winfo_screenwidth(), graph.winfo_screenheight()))

    ts =  TimeSeries(key = 'GKLUSRM3E6Y6548B', output_format= 'pandas')
    ticker, metadata = ts.get_daily_adjusted(symbol, outputsize = 'full')
    ticker = ticker.sort_index(axis=0 ,ascending=True)
    ticker = ticker.drop(['7. dividend amount', '8. split coefficient'], axis=1)
    ticker.columns=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    ticker['100ma'] = ticker['Adj Close'].rolling(window= 100, min_periods= 0).mean()
    ticker.to_csv(f"{symbol}.csv")
    ticker_file = pd.read_csv(f"{symbol}.csv", parse_dates = True, index_col= 0)
    ticker_file.reset_index(inplace=True)
    fig  = plt.Figure(figsize = (5,4), dpi=100)
    ax1 = fig.add_subplot(111)
    ax1.plot(ticker_file['date'],ticker_file['Adj Close'])
    ax1.plot(ticker_file['date'],ticker_file['100ma'])
    canvas = FigureCanvasTkAgg(fig, graph)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand =1)
    toolbar = NavigationToolbar2Tk(canvas, graph)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand =1)
    Back_Button = Button(graph, text = "Go Back", command = lambda: raise_frame(root, graph)).pack()   
    return

def indice(symbol):
    ts =  TimeSeries(key = 'GKLUSRM3E6Y6548B', output_format= 'pandas')
    ticker, metadata = ts.get_daily_adjusted(symbol, outputsize = 'full')
    ticker = ticker.sort_index(axis=0 ,ascending=True)
    ticker = ticker.drop(['7. dividend amount', '8. split coefficient'], axis=1) 
    ticker.columns=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    ticker.reset_index(inplace=True)
    ticker.to_csv(f"{symbol}.csv")
    ticker_file = pd.read_csv(f"{symbol}.csv", parse_dates = True, index_col= 0)
    ticker_file.set_index('date', inplace = True)
    print(ticker_file.tail())
    ticker.plot(x='date', y='Adj Close')
    plt.show()
    return

def check(symbol, choice,root):
    symbol = str(symbol.get())
    tickers = ['DJI','NDX','SPX','OEX','RUT','TSX']
    for tick in tickers:
        if symbol != tick:
            get_ticker_data(symbol,root)
            break
        else:
            newboy = Toplevel()
            newboy.title("Error")
            TickerName = Label(newboy, text = " Not a valid Stock").place(x = 30, y = 90)
            newboy.mainloop()
            break
    return

def checkIndice(symbol):
    symbols = symbol.get()
    tickers = ['DJI','NDX','SPX','OEX','RUT','TSX']
    for tick in tickers:
        if symbols == tick:
            print(tick)
            indice(symbols)
            break
        else:
            newboy = Toplevel()
            newboy.title("Error")
            TickerName = Label(newboy, text = "Not a valid index").place(x = 30, y = 90)
    return
            
def openFile(): 
    new = Toplevel()
    symbol = StringVar()
    Labe = Label(new, text = "Please Enter Indice Symbol").place(x = 50, y = 50)
    text = Entry(new, textvariable = symbol).place(x= 120, y= 50)
    Submit = Button(new, text = "Submit", command = lambda: checkIndice(symbol)).place(x=50, y= 75)
    figure = plt.Figure(figsize=(6,5), dpi=100)
    new.mainloop()
    return

def raise_frame(frame, current):
    frame.tkraise()
    current.destroy()
