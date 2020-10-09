import pandas as pd
from tkinter import *

def get_ticker_symbol(companyname):
    df = pd.read_csv('secwiki_tickers.csv')
    df.drop(['Price','Collection'],axis =1,inplace = True)
    companyname = companyname.get()
    print(companyname)
    found  = 0
    i = 0
    for name in df['Name']:
        if companyname == name.split(" ")[0]:
            found = 1
            break
        i=i+1
    if found == 1:
        FoundSym = Tk()
        FoundSym.title("Company Info")
        Label(FoundSym, text = "Please enter symbol %s" %df['Ticker'].loc[i]).pack()
        Label(FoundSym, text = "Company Name: %s" %df['Name'].loc[i]).pack()
        Label(FoundSym, text = "Industry: %s" %df['Industry'].loc[i]).pack()
        Label(FoundSym, text = "Sector: %s" %df['Sector'].loc[i]).pack()
        QuitButton = Button(FoundSym, text = "Back", command = lambda: FoundSym.destroy()).pack()
        FoundSym.mainloop()
    return

