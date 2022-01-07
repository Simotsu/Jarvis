import sys as sys1
import praw 
from config import *
from algos import *
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import robin_stocks.robinhood as r

def show_redditsocial():
    print(" ")
    ans=input("What subreddit would you like to search?: ")
    print(" ")
    ans1=input("What keyword would you like to search?: ")
    print(" ")

    search_term=ans
    keyword=ans1

    if (len(sys1.argv)>1):
        search_term=(sys1.argv[1])

    if (len(sys1.argv)>2):
        keyword=(sys1.argv[2])

    print(" Subreddit: ",search_term)
    print(" Keyword: ",keyword)
    

    subreddit = reddit.subreddit(search_term)

    resp = subreddit.search(keyword,limit=10)

    for submission in resp:
        print( "=ID: ",submission.id)
        print( "  Title: ",submission.title.encode('ascii', 'ignore'))
        print( "  Score: ",submission.score)
        print( "  URL: ",submission.url.encode('ascii', 'ignore'))
        print( "  Text: ",submission.selftext[:120].encode('ascii', 'ignore'))
        print(" ")
#def show_watchlist():
    """
    If you sell a stock, this updates tradehistory.txt with information about the position,
    how much you've earned/lost, etc.
    """
                                                                                                                                                                             
  #  register_matplotlib_converters()
  #  watchlist_symbols = get_watchlist_symbols()
  #  portfolio_symbols = get_portfolio_symbols()
 #   holdings_data = get_modified_holdings()
 #   potential_buys = []
 #   sells = []
 #   print("\n"
#    "\n"

 #   " ▄████▄   █    ██  ██▀███   ██▀███  ▓█████  ███▄    █ ▄▄▄█████▓    █     █░ ▄▄▄     ▄▄▄█████▓ ▄████▄   ██░ ██  ██▓     ██▓  ██████ ▄▄▄█████▓\n"
 #   "▒██▀ ▀█   ██  ▓██▒▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒   ▓█░ █ ░█░▒████▄   ▓  ██▒ ▓▒▒██▀ ▀█  ▓██░ ██▒▓██▒    ▓██▒▒██    ▒ ▓  ██▒ ▓▒\n"
 #   "▒▓█    ▄ ▓██  ▒██░▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░   ▒█░ █ ░█ ▒██  ▀█▄ ▒ ▓██░ ▒░▒▓█    ▄ ▒██▀▀██░▒██░    ▒██▒░ ▓██▄   ▒ ▓██░ ▒░\n"
 #   "▒▓▓▄ ▄██▒▓▓█  ░██░▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░    ░█░ █ ░█ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█ ░██ ▒██░    ░██░  ▒   ██▒░ ▓██▓ ░ \n"
#    "▒ ▓███▀ ░▒▒█████▓ ░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒██░   ▓██░  ▒██▒ ░    ░░██▒██▓  ▓█   ▓██▒ ▒██▒ ░ ▒ ▓███▀ ░░▓█▒░██▓░██████▒░██░▒██████▒▒  ▒██▒ ░ \n"
 ##   "░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░      ░ ▓░▒ ▒   ▒▒   ▓▒█░ ▒ ░░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   \n"
#    "  ░  ▒   ░░▒░ ░ ░   ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░ ░░   ░ ▒░    ░         ▒ ░ ░    ▒   ▒▒ ░   ░      ░  ▒    ▒ ░▒░ ░░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░    ░    \n"
 #   "░         ░░░ ░ ░   ░░   ░   ░░   ░    ░      ░   ░ ░   ░           ░   ░    ░   ▒    ░      ░         ░  ░░ ░  ░ ░    ▒ ░░  ░  ░    ░      \n"
  #  "░ ░         ░        ░        ░        ░  ░         ░                 ░          ░  ░        ░ ░       ░  ░  ░    ░  ░ ░        ░           \n"
 #   "░                                                                                            ░                                              \n"
  #  "\n"
  #  "\n"     + str(watchlist_symbols) + "\n" + "\n" + "\n")
 

#Show User Portfolio, Can select additional info for detailed look.
def show_portfolio():                                                                                                                                                                             
    portfolio_symbols = get_portfolio_symbols()
    myStocks =  r.build_holdings()
    myStockValues = []
    print(" \n"     
    "\n"
    "\n"
    "\n"       

    "\n"
    " ███▄ ▄███▓▓██   ██▓    ██▓███   ▒█████   ██▀███  ▄▄▄█████▓  █████▒▒█████   ██▓     ██▓ ▒█████   \n" 
    "▓██▒▀█▀ ██▒ ▒██  ██▒   ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▓██   ▒▒██▒  ██▒▓██▒    ▓██▒▒██▒  ██▒ \n" 
    "▓██    ▓██░  ▒██ ██░   ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▒████ ░▒██░  ██▒▒██░    ▒██▒▒██░  ██▒ \n" 
    "▒██    ▒██   ░ ▐██▓░   ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ░▓█▒  ░▒██   ██░▒██░    ░██░▒██   ██░ \n" 
    "▒██▒   ░██▒  ░ ██▒▓░   ▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ░▒█░   ░ ████▓▒░░██████▒░██░░ ████▓▒░ \n" 
    "░ ▒░   ░  ░   ██▒▒▒    ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░    ▒ ░   ░ ▒░▒░▒░ ░ ▒░▓  ░░▓  ░ ▒░▒░▒░  \n" 
    "░  ░      ░ ▓██ ░▒░    ░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░     ░       ░ ▒ ▒░ ░ ░ ▒  ░ ▒ ░  ░ ▒ ▒░  \n" 
    "░      ░    ▒ ▒ ░░     ░░       ░ ░ ░ ▒    ░░   ░   ░       ░ ░   ░ ░ ░ ▒    ░ ░    ▒ ░░ ░ ░ ▒   \n" 
    "       ░    ░ ░                     ░ ░     ░                         ░ ░      ░  ░ ░      ░ ░   \n" 
    "            ░ ░                                                                                  \n"
    "                                          \n" 
    " \n " + str(portfolio_symbols) + "\n" + "\n" + "\n")

    ans=input("Would you like to see additional information?(Y or N): ")
    if ans=='Y': 
        for key, value in myStocks.items():
            print("\n\n-----Stock Ticker------")
            print(key)
            myBS = value
            print("==========")
            for key, value in myBS.items():
                capital = key
                print(capital.capitalize())
                print(value)
        print("\n\n")
    if ans=='':      
        print('')

def show_selladvice():                                                                                                         
    register_matplotlib_converters()
    watchlist_symbols = get_watchlist_symbols()
    portfolio_symbols = get_portfolio_symbols()
    holdings_data = get_modified_holdings()
    potential_buys = []
    sells = []
    print("""
                                                     

                                                                                                                 
        ADD SELL SHIT HERE                                                                                                         

    """)
    for symbol in portfolio_symbols:
        cross = golden_cross(symbol, n1=50, n2=200, days=30, direction="below")
        if(cross == -1):
            if startselling:
                sell_holdings(symbol, holdings_data)
                sells.append(symbol)
    profile_data = r.build_user_profile()
    return


def show_dataframe():
    start = datetime.datetime(2021, 6, 29)
    end = datetime.datetime(2021, 6, 30)
    print('Please Enter Today\'s Date')
    ans=input("Year: ")
    ans2=input("Month: ")
    ans3=input("Day: ")
    test1 = datetime.datetime(int(ans), int(ans2), int(ans3))
    df = web.DataReader("BBGI", 'av-daily', start, end)
    dt = web.DataReader("AMC", 'av-daily', start, end)
    dx = web.DataReader("GME", 'av-daily', start, end)
    dg = web.DataReader("BB", 'av-daily', start, end)
    dl = web.DataReader("MMAT", 'av-daily')
    dn = web.DataReader("CIDM", 'av-daily', test1)
    print(dl)
    print(dn.Volume)
    df.to_csv('modified1.csv')
    dt.to_csv('modified2.csv')
    dx.to_csv('modified3.csv')
    dg.to_csv('modified4.csv')

    df = pd.read_csv('modified1.csv')
    dt = pd.read_csv('modified2.csv')
    dx = pd.read_csv('modified3.csv')
    dg = pd.read_csv('modified4.csv')

    print(df.Volume)
    plt.plot(df.Date, df.Volume, color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue', label="TRCH")
    plt.plot(df.Date, dt.Volume, color='orange', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue', label="AMC")
    plt.plot(df.Date, dx.Volume, color='green', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue', label="GME")
    plt.plot(df.Date, dg.Volume, color='blue', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue', label="BB")

    plt.title('Meme Stocks May to Present 2021!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
    plt.xticks(df.Date[::5])
   # plt.yticks([100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000])
    # X and Y labels
    plt.xlabel('Date')
    plt.ylabel('Volume in 100 Millions')
    plt.legend()
    plt.savefig('TRCH', dpi=300)
    plt.show()


def show_volume():
    #register_matplotlib_converters()
    watchlist_symbols = get_watchlist_symbols()
    #portfolio_symbols = get_portfolio_symbols()
    #holdings_data = get_modified_holdings()
    start = datetime.datetime(2021, 6, 29)
    end = datetime.datetime(2021, 6, 30)
    print('Please Enter Today\'s Date')
    ans=input("Year: ")
    ans2=input("Month: ")
    ans3=input("Day: ")
    test1 = datetime.datetime(int(ans), int(ans2), int(ans3))
    ans4=input("Would you like to search your Watchlist?(Y or N): ")
    if ans4  == ("Y"):
        for symbol in watchlist_symbols:
            dx = web.DataReader(symbol, "stooq", test1)
            if (dx.empty):
                dx = web.DataReader(symbol, "stooq", test1)
                print("Its not going to work out well..." + str(symbol))
            elif (dx.Volume[0] > 1000000):
                print('High Volume Here: ' + str(symbol))    
    if ans4  == ("N"):
        ans5=input("Which ticker would you like to look up?: ")
        dn = web.DataReader(ans5, "stooq")
        #print(dn.Volume)

    print("\n\n\n\n\n"


    " ██░ ██  ▒█████  ▄▄▄█████▓     ██████ ▄▄▄█████▓ ▒█████   ▄████▄   ██ ▄█▀  ██████ \n"
    "▓██░ ██▒▒██▒  ██▒▓  ██▒ ▓▒   ▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▒██▀ ▀█   ██▄█▒ ▒██    ▒ \n"
    "▒██▀▀██░▒██░  ██▒▒ ▓██░ ▒░   ░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▒▓█    ▄ ▓███▄░ ░ ▓██▄   \n"
    "░▓█ ░██ ▒██   ██░░ ▓██▓ ░      ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄   ▒   ██▒\n"
    "░▓█▒░██▓░ ████▓▒░  ▒██▒ ░    ▒██████▒▒  ▒██▒ ░ ░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄▒██████▒▒\n"
    " ▒ ░░▒░▒░ ▒░▒░▒░   ▒ ░░      ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░\n"
    " ▒ ░▒░ ░  ░ ▒ ▒░     ░       ░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░░ ░▒  ░ ░\n"
    " ░  ░░ ░░ ░ ░ ▒    ░         ░  ░  ░    ░      ░ ░ ░ ▒  ░        ░ ░░ ░ ░  ░  ░  \n"
    " ░  ░  ░    ░ ░                    ░               ░ ░  ░ ░      ░  ░         ░  \n"
    "                                                        ░                        \n"
    "\n")
 
    dx = web.DataReader('AMC', "stooq", test1)
    print(dx.head)
    print(dx.Volume)
    print(" ")
    print(dx.Volume[0])

    if (dx.Volume[0] > volFinder):
        print('High Volume Here')    
    #N0T1A3DIQKU0QFVS





def show_stocksearch():
    #show stock search 
    ans=input("""
  ██████ ▄▄▄█████▓ ▒█████   ▄████▄   ██ ▄█▀     ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ 
▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▒██▀ ▀█   ██▄█▒    ▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒
░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▒▓█    ▄ ▓███▄░    ░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░
  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄      ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ 
▒██████▒▒  ▒██▒ ░ ░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄   ▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓
▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒
░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░   ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░
░  ░  ░    ░      ░ ░ ░ ▒  ░        ░ ░░ ░    ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░
      ░               ░ ░  ░ ░      ░  ░            ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░
                           ░                                                    ░                

What stock would you like to lookup?: """) 
    #Get Quote of Stock
    quote = get_stockquote(ans)

    #Couldn't get quote data
    if(quote is None or None in quote):
        return False
    #Make the quote into an array using key, value for a dictionary
    miniArray = []
    for key, value in quote.items():
        miniArray.append(value)

    #print the quote from the array one variable at a time
    print("Stock Ticker: " + miniArray[9])
    print("Ask Price: " + miniArray[0])
    print("Bid Price: " + str(miniArray[1]))
    print("Last Trade Price: " + miniArray[4])
    print("Previous Close: " + str(miniArray[6]))
    if(miniArray[5] is None):
        print('')
    else:
        print("Last Extended Hours Trade Price: " + miniArray[5])


def show_visualizestock():
    
    ans=input("""
Stock Ticker: Symbol of the stock we're querying.
Interval: Interval to retrieve data for. Values are ‘5minute’, ‘10minute’, ‘hour’, ‘day’, ‘week’. 
Span: Sets the range of the data to be either ‘day’, ‘week’, ‘month’, ‘3month’, ‘year’, or ‘5year’.
Bounds: Represents if graph will include extended trading hours or just regular trading hours. Values are ‘extended’, ‘trading’, or ‘regular’.
IntervalNum: Number representation of Interval .035 = 5minute .069 = 10minute .417 = 1hour. 1 = 1day.
SpanNum: Number representation of Span.


Stock Ticker: """) 
    ans2=input("Interval: ")     
    ans3=input("Span: ")   
    ans4=input("Bounds: ")
    ans5=input("IntervalNum: ")   
    ans6=input("SpanNum: ")   
    history = get_historicals(ans, ans2, ans3, ans4)
    #print(web.get_data_fred(ans))
    #Couldn't get pricing data
    if(history is None or None in history):
        return False
    
    closingPrices = []
    dates = []
    for item in history:
        closingPrices.append(float(item['close_price']))
        dates.append(item['begins_at'])
    price = pd.Series(closingPrices)
    dates = pd.Series(dates)
    dates = pd.to_datetime(dates)
    sma1 = ta.volatility.bollinger_mavg(price, int(ans5), False)
    sma2 = ta.volatility.bollinger_mavg(price, int(ans6), False)
    print(sma1)
    print(sma2)
    show_plot(price, sma1, sma2, dates, symbol=ans, label1=str(ans5)+" day SMA", label2=str(ans6)+" day SMA")

###
###Algorithm Search
###
def show_stockalgorithmchecker():
    #show stock search 
    ans=input("""                                      


     ▄▄▄       ██▓      ▄████  ▒█████   ██▀███   ██▓▄▄▄█████▓ ██░ ██  ███▄ ▄███▓     ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ 
    ▒████▄    ▓██▒     ██▒ ▀█▒▒██▒  ██▒▓██ ▒ ██▒▓██▒▓  ██▒ ▓▒▓██░ ██▒▓██▒▀█▀ ██▒   ▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒
    ▒██  ▀█▄  ▒██░    ▒██░▄▄▄░▒██░  ██▒▓██ ░▄█ ▒▒██▒▒ ▓██░ ▒░▒██▀▀██░▓██    ▓██░   ░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░
    ░██▄▄▄▄██ ▒██░    ░▓█  ██▓▒██   ██░▒██▀▀█▄  ░██░░ ▓██▓ ░ ░▓█ ░██ ▒██    ▒██      ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ 
    ▓█   ▓██▒░██████▒░▒▓███▀▒░ ████▓▒░░██▓ ▒██▒░██░  ▒██▒ ░ ░▓█▒░██▓▒██▒   ░██▒   ▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓
    ▒▒   ▓▒█░░ ▒░▓  ░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▓    ▒ ░░    ▒ ░░▒░▒░ ▒░   ░  ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒
    ▒   ▒▒ ░░ ░ ▒  ░  ░   ░   ░ ▒ ▒░   ░▒ ░ ▒░ ▒ ░    ░     ▒ ░▒░ ░░  ░      ░   ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░
    ░   ▒     ░ ░   ░ ░   ░ ░ ░ ░ ▒    ░░   ░  ▒ ░  ░       ░  ░░ ░░      ░      ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░
        ░  ░    ░  ░      ░     ░ ░     ░      ░            ░  ░  ░       ░            ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░
                                                                                                                 ░                


    Main Menu:
    1: GoldenCross Search
    2: Percentage Search
    8: Quit 


What would you like to do?:""") 
    if ans=="1": 
        show_goldencrosssearch()
        print("\n My Stocks Selected")
    if ans=="2":
        #Do Something
        return 0

###
###Testing
###
def test():
    start = datetime.datetime(2019, 6, 2)
    end = datetime.datetime(2021, 6, 2)
    df = web.DataReader("TRCH", 'yahoo', start, end)
    dx = web.DataReader("AMC", "yahoo", start, end)
    print(dx)
    print("-----")
    print(df)
    df = web.DataReader('GDP', 'fred', start, end)
    print("-----")
    print(df)
    data = pd.DataFrame(raw['XAU='])
    data.rename(columns={'XAU=': 'price'}, inplace=True)
    data['returns'] = np.log(data['price'] / data['price'].shift(1))
    data['position'] = np.sign(data['returns'].rolling(3).mean())
    data['strategy'] = data['position'].shift(1) * data['returns']
    data[['returns', 'strategy']].dropna().cumsum().apply(np.exp).plot(figsize=(10, 6));

###
###GoldenCross
###
def show_goldencrosssearch():
    #show stock search
    ans=input(""" 
Questions Explained:
Stock Ticker: Symbol of the stock we're querying
Short Term Indicator: Specifies the short-term indicator as an X-day moving average.
Long Term Indicator: Specifies the long-term indicator as an X-day moving average.
(Short Term Indicatory Value should be smaller than Long Term Indicator Value to produce meaningful results, e.g sti=50, lti=200)
Days: Specifies the maximum number of days that the golden cross can occur by.
Direction: "above" if we are searching for an upwards cross, "below" if we are searching for a downwards cross. Do no use capitals

What stock would you like to lookup?: """) 
    ans2=input("Short Term Indicator: ")
    ans3=input("Long Term Indicator: ")
    ans4=input("Maximum Number of Days: ")    
    ans5=input("Direction: ")
    stockhood_goldencross(ans, ans2, ans3, ans4, ans5)
