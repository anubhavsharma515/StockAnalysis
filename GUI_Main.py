import pandas as pd
import numpy as np
from tkinter import *
import matplotlib.dates as mdates
from AdjVol import openFile, check
from PCT_Change import pct_change
from CompanyTicker import get_ticker_symbol
from Candlesticks import candle_stick
from PIL import Image,ImageTk
#from AllGraph import All

def where_send(symbol, choice, date_option,root):
    choice = (choice.get())
    print(choice)
    if choice == "Adj Close":
        check(symbol, date_option,root)
    elif choice == "Candle Stick":
        candle_stick(symbol, date_option,root)
    elif choice == "Percent Change":
        pct_change(symbol, date_option)
    elif choice == "All":
        All(symbol, date_option)
    return

#Data Window
def new(UserNames, main):
    User = str(UserNames.get())
    if(len(User)<2):
        Err = Toplevel()
        Label(Err, text= "invalid").pack()
        but = Button(main, text = 'close').place(x=175, y=224)
    else:
        root = Toplevel()
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.title("%s \'s Data" % User)
        img = ImageTk.PhotoImage(Image.open("intkTW.jpg"))
        panel = Label(root, image=img).place(y=0)
        menu = Menu(root)
        root.config(menu=menu) 
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu) 
        filemenu.add_command(label="New")
        filemenu.add_command(label="Back To Home", command = lambda: raise_frame(main, root))
        indice = Menu(menu)
        menu.add_cascade(label='Indices', menu=indice)
        indice.add_command(label="Get Index Data", command = lambda: openFile())
        symbol = StringVar()
        choice = StringVar()
        date_choice = StringVar()
        Company = StringVar()
        tickername = Entry(root,textvariable=symbol,font=("Helvetica", 15)).place(x = 300, y = 120)
        Welcome  = Label(root, text = "Welcome %s" % User,font=("Helvetica", 32)).place(x = 30, y = 50)
        TickerName = Label(root, text = "Enter Ticker Symbol",font=("Helvetica", 20)).place(x = 30, y = 120)
        CompanyEntry = Entry(root, textvariable = Company, font=("Helvetica", 15))
        CompanyName = Label(root, text = "Enter Company Name", font = ("Helvetica",20)).place(x=30, y=170)
        CompanyEntry.place(x = 320, y = 170)
        CompanyTicker = Button(root, text = "Find Ticker", command = lambda: get_ticker_symbol(Company),font = ("Helvetica",15)).place(x = 590, y= 170)
        choice.set("Adj Close")
        date_choice.set("20 Years")
        data_option = OptionMenu(root, choice, "Adj Close", "Candle Stick", "Percent Change", "All").place(x = 530, y = 120)
        date_option = OptionMenu(root, date_choice, "20 Years", "10 Years", "5 Years", "1 year", "100 days").place(x = 620, y = 120)
        quitButton = Button(root, text="Get Data", command = lambda: where_send(symbol,choice,date_choice,root),font=("Helvetica", 20)).place(x=30, y=400)
        root.mainloop()
    return

#Main Window - User enter Name
main = Tk()
main.title("SharData")
main.geometry("{0}x{1}+0+0".format(main.winfo_screenwidth(), main.winfo_screenheight()))

img = ImageTk.PhotoImage(Image.open("intkTW.jpg"))
panel = Label(main, image=img).place(y=0)
display = Label(main, text="Hi there, Welcome to SharStock!",font=("Helvetica", 32)).grid(row = 0, column = 0)
UserName = StringVar()
Name =Label(main, text ="Please enter your name", font=("Helvetica", 32)).grid(row = 1, column = 0, sticky=W)
Name_Entry = Entry(main, textvariable = UserName, font=("Helvetica", 32)).grid(row = 1, column = 1)
quitButton = Button(main, text="Enter", command = lambda: new(UserName, main),font=("Helvetica", 32)).grid(row = 3, column = 0, sticky = W)
main.mainloop()

input("Press enter to continue...")
