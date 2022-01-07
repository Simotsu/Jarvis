import robin_stocks.robinhood as r
import pandas as pd
import numpy as np
import ta as ta
import time
import datetime
import pandas_datareader.data as web
import sys
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from ta import *
from misc import *
from tradingstats import *
from config import *
from algos import *
from methods import *
from pandas import Series, DataFrame
from tkinter import *
import os
ans=True

def show_hotstocks():                                                                                                                    
    register_matplotlib_converters()
    watchlist_symbols = get_watchlist_symbols()

    ans=input("""
This will calculate rising or falling stocks based on 5 minute intervals.
IE: 1 = 10 minutes | 2 = 15 minutes | 3 = 20 minutes | 4 = 25 minutes | etc...
How many 5 minute intervals?: """) 
    ans2=input("""
Please enter the percentage up you are looking for.
IE: 3 - Stock went up 3'%' over indicated 5 minute interval | 5 - Stock went up 5'%' over indicated 5 minute interval | etc..
What Percentage Up?: """)
    ans3=input("""
Please enter the percentage down you are looking for.
IE: 3 - Stock went down 3'%' over indicated 5 Minute Interval | 5 - Stock went down 5'%' over indicated 5 Minute Interval | etc..
What Percentage Down?: """) 
    for symbol in watchlist_symbols:
        stockhood_main2(symbol, ans, ans2, ans3)
        #potential_buys.append(symbol)
    if(len(potential_buys) > 0):
        if startbuying:
            print('okBUY')
        buy_holdings(potential_buys, profile_data, holdings_data)
        if(len(sells) > 0):
            update_trade_history(sells, holdings_data, "tradehistory.txt")
            print("----- Scan Complete -----\n")
    if debug:
        print("----- DEBUG MODE ON -----\n")

        
def show_watchlist():
    """
    If you sell a stock, this updates tradehistory.txt with information about the position,
    how much you've earned/lost, etc.
    """
                                                                                                                                                                             
    #register_matplotlib_converters()
    watchlist_symbols = get_watchlist_symbols()
    print("\n"
    "\n"

    " ▄████▄   █    ██  ██▀███   ██▀███  ▓█████  ███▄    █ ▄▄▄█████▓    █     █░ ▄▄▄     ▄▄▄█████▓ ▄████▄   ██░ ██  ██▓     ██▓  ██████ ▄▄▄█████▓\n"
    "▒██▀ ▀█   ██  ▓██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒   ▓█░ █ ░█░▒████▄   ▓  ██▒ ▓▒▒██▀ ▀█  ▓██░ ██▒▓██▒    ▓██▒▒██    ▒ ▓  ██▒ ▓▒\n"
    "▒▓█    ▄ ▓██  ▒██░▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░   ▒█░ █ ░█ ▒██  ▀█▄ ▒ ▓██░ ▒░▒▓█    ▄ ▒██▀▀██░▒██░    ▒██▒░ ▓██▄   ▒ ▓██░ ▒░\n"
    "▒▓▓▄ ▄██▒▓▓█  ░██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░    ░█░ █ ░█ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█ ░██ ▒██░    ░██░  ▒   ██▒░ ▓██▓ ░ \n"
    "▒ ▓███▀ ░▒▒█████▓ ░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒██░   ▓██░  ▒██▒ ░    ░░██▒██▓  ▓█   ▓██▒ ▒██▒ ░ ▒ ▓███▀ ░░▓█▒░██▓░██████▒░██░▒██████▒▒  ▒██▒ ░ \n"
    "░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░      ░ ▓░▒ ▒   ▒▒   ▓▒█░ ▒ ░░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   \n"
    "  ░  ▒   ░░▒░ ░ ░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░ ░░   ░ ▒░    ░         ▒ ░ ░    ▒   ▒▒ ░   ░      ░  ▒    ▒ ░▒░ ░░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░    ░    \n"
    "░         ░░░ ░ ░   ░░   ░   ░░   ░    ░      ░   ░ ░   ░           ░   ░    ░   ▒    ░      ░         ░  ░░ ░  ░ ░    ▒ ░░  ░  ░    ░      \n"
    "░ ░         ░        ░        ░        ░  ░         ░                 ░          ░  ░        ░ ░       ░  ░  ░    ░  ░ ░        ░           \n"
    "░                                                                                            ░                                              \n"
    "\n"
    "\n"     + str(watchlist_symbols) + "\n" + "\n" + "\n")
#execute the scan
#maybe get an input from user?
#scan_stocks()
#Log in to Robinhood
#Put your username and password in a config.py file in the same directory (see sample file)

login = r.login(rh_username,rh_password)

print("""
                                                                            
                                                                                                       
              JJJJJJJJJJJ                                                           iiii                   
              J:::::::::J                                                          i::::i                  
              J:::::::::J                                                           iiii                   
              JJ:::::::JJ                                                                                  
                J:::::J  aaaaaaaaaaaaa  rrrrr   rrrrrrrrrvvvvvvv           vvvvvvviiiiiii     ssssssssss   
                J:::::J  a::::::::::::a r::::rrr:::::::::rv:::::v         v:::::v i:::::i   ss::::::::::s  
                J:::::J  aaaaaaaaa:::::ar:::::::::::::::::rv:::::v       v:::::v   i::::i ss:::::::::::::s 
                J:::::j           a::::arr::::::rrrrr::::::rv:::::v     v:::::v    i::::i s::::::ssss:::::s
                J:::::J    aaaaaaa:::::a r:::::r     r:::::r v:::::v   v:::::v     i::::i  s:::::s  ssssss 
    JJJJJJJ     J:::::J  aa::::::::::::a r:::::r     rrrrrrr  v:::::v v:::::v      i::::i    s::::::s      
    J:::::J     J:::::J a::::aaaa::::::a r:::::r               v:::::v:::::v       i::::i       s::::::s   
    J::::::J   J::::::Ja::::a    a:::::a r:::::r                v:::::::::v        i::::i ssssss   s:::::s 
    J:::::::JJJ:::::::Ja::::a    a:::::a r:::::r                 v:::::::v        i::::::is:::::ssss::::::s
     JJ:::::::::::::JJ a:::::aaaa::::::a r:::::r                  v:::::v         i::::::is::::::::::::::s 
       JJ:::::::::JJ    a::::::::::aa:::ar:::::r                   v:::v          i::::::i s:::::::::::ss  
         JJJJJJJJJ       aaaaaaaaaa  aaaarrrrrrr                    vvv           iiiiiiii  sssssssssss    


     Coded By: Simotsu@gmail.com
    """)
while ans:
    print ("""

    Main Menu:
    1: My Stocks
    2: My Watchlist
    3: Stock Scanner
    4: Visualize Stock
    5: Initialize Bot
    6: Backtesting 
    7: Stock Lookup
    8: Earnings Reports
    9: Quit
    10: Test
    """)
    ans=input("What would you like to do? ") 
    #Portfoilio Selected
    if ans=="1": 
        show_portfolio()
        print("\n My Stocks Selected")
    #Watchlist Selected
    elif ans=="2":
        show_watchlist()
        print("\n My Watchlist Selected")
    #Stock Scanner Selected
    elif ans=="3":
        print ("""
    Stock Scanner Selected:
    Please Choose From The Following:
        A: Algorithm
        B: Quantitative
        C: Percentage
        D: Volume
        E: Social
        F: Go Back
        """)
        ans2=input("How would you like to scan? ") 
        if ans2=="A": 
            print("\n Algorithm Selected") 
            print ("""
            Please Choose From The Following:
                A: Time-Series Momentum/Mean Reversion
                B: Cross-Sectional Momentum/Mean Reversion
                C: Gap-up Momentum
                D: Statistical Arbitrage
                E: Weighted Average Price
                F: Golden Cross Up
                G: Golden Cross Down
                H: Go Back
            """)
            ans3=input("Which Algoritmic Pattern Would You Like To Implement? ") 
            if ans3=="A": 
                print("\n Time-Series Momentum/Mean Reversion Selected")
                ans4=input("Please enter the stock ticker: ") 
                timeseriesmomentummeanreversion(ans4)
            if ans3=="B": 
                print("\n Time-Series Momentum/Mean Reversion Selected in Depth") 
                ans4=input("Please enter the stock ticker: ") 
                ans5=input("Please enter SMA day count(20,30,50): ")
                ans6=input("Please enter a time period(month, year, 5year): ")                 
                ans7=input("Please enter the threshold(0.1, 0.12, 0.14): ") 
                ans8=input("Please enter true or false for Short Positons: ") 
                SMAMeanReversion()
            if ans3=="C": 
                print("\n Gap-up Momentum Selected")
            if ans3=="D": 
                print("\n Statistical Arbitrage Selected")
            if ans3=="E": 
                print("\n Weighted Average Price Selected")
            if ans3=="F": 
                print("\n Golden Cross Up Selected")
            if ans3=="G": 
                print("\n Golden Cross Down Selected")
#Quantitative
        if ans2=="B": 
            print("\n Quantitative Selected")
            print ("""
            Please Choose From The Following:
                A: Bi-Directional Encoder Representations from Transformers (BERT)
                B: Long Short Term Memory (LSTM)
                C: Gated Recurrent Units (GRU)
                D: Auto Regressive Integrated Moving Average (ARIMA)
                E: GAN
                F: Go Back
            """)
            ans3=input("Which Quantitative Strategy Would You Like To Implement? ") 
            if ans3=="A": 
                print("\n Bi-Directional Encoder Representations from Transformers (BERT) Selected")
            if ans3=="B": 
                print("\n Long Short Term Memory (LSTM) Selected") 
            if ans3=="C": 
                print("\n Gated Recurrent Units (GRU) Selected")
            if ans3=="D": 
                print("\n Auto Regressive Integrated Moving Average (ARIMA) Selected")
            if ans3=="E": 
                print("\n GAN Selected")
#Percentage
        if ans2=="C": 
            print("\n Percentage Selected")
            show_hotstocks()
            ans3=input("Which Quantitative Strategy Would You Like To Implement? ") 
            if ans3=="A": 
                print("\n Bi-Directional Encoder Representations from Transformers (BERT) Selected")
            if ans3=="B": 
                print("\n Long Short Term Memory (LSTM) Selected") 
            if ans3=="C": 
                print("\n Gated Recurrent Units (GRU) Selected")
            if ans3=="D": 
                print("\n Auto Regressive Integrated Moving Average (ARIMA) Selected")
            if ans3=="E": 
                print("\n GAN Selected")
#Volume
        if ans2=="D": 
            print("\n Volume Selected") 
            print ("""
            Please Choose From The Following:
                A: Volume 1
                B: Go Back
            """)
            ans3=input("Which Volume Search Would You Like To Implement? ") 
            if ans3=="A": 
                print("\n Volume 1 Selected")
            if ans3=="B": 
                print("\n Selected") 
            if ans3=="C": 
                print("\n Selected")
            if ans3=="D": 
                print("\n Selected")
            if ans3=="E": 
                print("\n Selected")
#Social
        if ans2=="E": 
            print("\n Social Selected")
            print ("""
            Please Choose From The Following:
                A: Twitter
                B: WSB
                C: Reddit
                D: Go Back
            """)
            ans3=input("Which Social Media Platform Search Would You Like To Implement? ") 
            if ans3=="A": 
                print("\n Twitter Selected")
            if ans3=="B": 
                print("\n Wall Street Bets Selected") 
            if ans3=="C": 
                print("\n Reddit Selected")
                show_redditsocial()
    #Visualize Stock Selected
    elif ans=="4":
        print ("""
    Visualize Stock Selected:
    Please Choose From The Following:
        A: Line Chart
        B: Candlestick Chart
        C: Bokeh's Chart
        D: Go Back
        """)
        ans3=input("Which option would you like to use: ") 
    #Init Bot Selected
    elif ans =="5":
        print ("""
    Initialize Bot Selected:
    Please Choose From The Following:
        A: Blah
        B: Bleh
        C: Blep
        D: Blop
        E: Blup
        F: Go Back
        """)
        ans3=input("Which option would you like to use: ") 
    #Backtesting Selected
    elif ans =="6":
        print("\n Back Testing")
        #Learn how to implement backtesting stuffs
    #Help/FAQS Selected
    elif ans =="7":
        print("\n Stock Lookup")
        show_stocksearch()
    #Help/FAQS Selected
    elif ans =="8":
        print("\n Help/FAQS")
        signal()
    #Quit Selected
    elif ans =="9":
        print("\n Quit Selected")
        raise SystemExit
    #Test Selected
    elif ans =="10":
        print("\n Help/FAQS")
        print ("""


Help and Frequently Asked Questions:
    
    
  █████▒▄▄▄        █████    ██████ 
▓██   ▒▒████▄    ▒██▓  ██▒▒██    ▒ 
▒████ ░▒██  ▀█▄  ▒██▒  ██░░ ▓██▄   
░▓█▒  ░░██▄▄▄▄██ ░██  █▀ ░  ▒   ██▒
░▒█░    ▓█   ▓██▒░▒███▒█▄ ▒██████▒▒
 ▒ ░    ▒▒   ▓▒█░░░ ▒▒░ ▒ ▒ ▒▓▒ ▒ ░
 ░       ▒   ▒▒ ░ ░ ▒░  ░ ░ ░▒  ░ ░
 ░ ░     ░   ▒      ░   ░ ░  ░  ░  
             ░  ░    ░          ░  
                                   
1) When did you start trading?
    A) I started Trading February 2021.
2) Why did you start trading?
    b) I heard about the GME / AMC madness happening.
3) Insert More. :)
        """)
    #Quit if wrong input
    elif ans !="":
        print("\n Wrong Input")   
            


