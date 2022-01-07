import robin_stocks.robinhood as r
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from datetime import *
import dateutil.parser
def safe_division(n, d):
    return n / d if d else 0

def get_historicals(ticker, intervalArg, spanArg, boundsArg):
    try:
        history = r.get_stock_historicals(ticker,interval=intervalArg,span=spanArg,bounds=boundsArg)
    except:
        print("Crypto cannot be calculated atm.")
        raise
    #If it's not a stock ticker, try it as a crypto ticker
    if(history is None or None in history):
        #history = r.get_crypto_historicals(ticker,interval=intervalArg,span=spanArg,bounds=boundsArg)
        print("^^Above This is a Crypto Error Disregard^^")

    return history

def get_stockquote(ticker):

    quote = r.get_stock_quote_by_id(ticker)
    #If it's not a stock ticker, try it as a crypto ticker
    if(quote is None or None in quote):
        quote = r.get_crypto_quote_by_id(ticker)
        print("^^Above This is a Crypto Error Disregard^^")
    return quote

def get_watchlist_symbols():
    """
    Returns: the symbol for each stock in your watchlist as a list of strings
    """
    my_list_names = set()
    symbols = set()
    
    watchlistInfo = r.get_all_watchlists()
    for watchlist in watchlistInfo['results']:
        listName = watchlist['display_name']
        my_list_names.add(listName)

    for listName in my_list_names:
        watchlist = r.get_watchlist_by_name(name=listName)
        if(watchlist is None):
            print('')
        else:
            for item in watchlist['results']:
                symbol = item['symbol']
                symbols.add(symbol)

    return symbols

def get_portfolio_symbols():
    """
    Returns: the symbol for each stock in your portfolio as a list of strings
    """
    symbols = []
    holdings_data = r.get_open_stock_positions()
    for item in holdings_data:
        if not item:
            continue
        instrument_data = r.get_instrument_by_url(item.get('instrument'))
        symbol = instrument_data['symbol']
        symbols.append(symbol)
    return symbols

def get_position_creation_date(symbol, holdings_data):
    """Returns the time at which we bought a certain stock in our portfolio

    Args:
        symbol(str): Symbol of the stock that we are trying to figure out when it was bought
        holdings_data(dict): dict returned by r.get_open_stock_positions()

    Returns:
        A string containing the date and time the stock was bought, or "Not found" otherwise
    """
    instrument = r.get_instruments_by_symbols(symbol)
    url = instrument[0].get('url')
    for dict in holdings_data:
        if(dict.get('instrument') == url):
            return dict.get('created_at')
    return "Not found"

def get_modified_holdings():
    """ Retrieves the same dictionary as r.build_holdings, but includes data about
        when the stock was purchased, which is useful for the read_trade_history() method
        in tradingstats.py

    Returns:
        the same dict from r.build_holdings, but with an extra key-value pair for each
        position you have, which is 'bought_at': (the time the stock was purchased)
    """
    holdings = r.build_holdings()
    holdings_data = r.get_open_stock_positions()
    for symbol, dict in holdings.items():
        bought_at = get_position_creation_date(symbol, holdings_data)
        bought_at = str(pd.to_datetime(bought_at))
        holdings[symbol].update({'bought_at': bought_at})
    return holdings

def get_last_crossing(df, days, symbol="", direction=""):
    """Searches for a crossing between two indicators for a given stock

    Args:
        df(pandas.core.frame.DataFrame): Pandas dataframe with columns containing the stock's prices, both indicators, and the dates
        days(int): Specifies the maximum number of days that the cross can occur by
        symbol(str): Symbol of the stock we're querying. Optional, used for printing purposes
        direction(str): "above" if we are searching for an upwards cross, "below" if we are searching for a downwaords cross. Optional, used for printing purposes

    Returns:
        1 if the short-term indicator crosses above the long-term one
        0 if there is no cross between the indicators
        -1 if the short-term indicator crosses below the long-term one
    """
    prices = df.loc[:,"Price"]
    shortTerm = df.loc[:,"Indicator1"]
    LongTerm = df.loc[:,"Indicator2"]
    dates = df.loc[:,"Dates"]
    lastIndex = prices.size - 1
    index = lastIndex
    found = index
    recentDiff = (shortTerm.at[index] - LongTerm.at[index]) >= 0
    if((direction == "above" and not recentDiff) or (direction == "below" and recentDiff)):
        return 0
    index -= 1
    while(index >= 0 and found == lastIndex and not np.isnan(shortTerm.at[index]) and not np.isnan(LongTerm.at[index]) \
                        and ((pd.Timestamp("now", tz='UTC') - dates.at[index]) <= pd.Timedelta(str(days) + " days"))):
        if(recentDiff):
            if((shortTerm.at[index] - LongTerm.at[index]) < 0):
                found = index
        else:
            if((shortTerm.at[index] - LongTerm.at[index]) > 0):
                found = index
        index -= 1
    if(found != lastIndex):
        if((direction == "above" and recentDiff) or (direction == "below" and not recentDiff)):
            print(symbol + ": Short SMA crossed" + (" ABOVE " if recentDiff else " BELOW ") + "Long SMA at " + str(dates.at[found]) \
                +", which was " + str(pd.Timestamp("now", tz='UTC') - dates.at[found]) + " ago", ", price at cross: " + str(prices.at[found]) \
                + ", current price: " + str(prices.at[lastIndex]))
        return (1 if recentDiff else -1)
    else:
        return 0

def five_year_check(stockTicker):
    """Figure out if a stock has risen or been created within the last five years.

    Args:
        stockTicker(str): Symbol of the stock we're querying

    Returns:
        True if the stock's current price is higher than it was five years ago, or the stock IPO'd within the last five years
        False otherwise
    """
    instrument = r.get_instruments_by_symbols(stockTicker)
    if(instrument is None or len(instrument) == 0):
        return True
    list_date = instrument[0].get("list_date")
    if ((pd.Timestamp("now") - pd.to_datetime(list_date)) < pd.to_timedelta(df['years_variable']*365, unit = 'D')).dt.date:
        return True
    fiveyear =  get_historicals(stockTicker, "day", "5year", "regular")
    if (fiveyear is None or None in fiveyear):
        return True
    closingPrices = []
    for item in fiveyear:
        closingPrices.append(float(item['close_price']))
    recent_price = closingPrices[len(closingPrices) - 1]
    oldest_price = closingPrices[0]
    return (recent_price > oldest_price)

def golden_cross(stockTicker, n1, n2, days, direction=""):
    """Determine if a golden/death cross has occured for a specified stock in the last X trading days

    Args:
        stockTicker(str): Symbol of the stock we're querying
        n1(int): Specifies the short-term indicator as an X-day moving average.
        n2(int): Specifies the long-term indicator as an X-day moving average.
                 (n1 should be smaller than n2 to produce meaningful results, e.g n1=50, n2=200)
        days(int): Specifies the maximum number of days that the cross can occur by
        direction(str): "above" if we are searching for an upwards cross, "below" if we are searching for a downwaords cross. Optional, used for printing purposes

    Returns:
        1 if the short-term indicator crosses above the long-term one
        0 if there is no cross between the indicators
        -1 if the short-term indicator crosses below the long-term one
        False if direction == "above" and five_year_check(stockTicker) returns False, meaning that we're considering whether to
            buy the stock but it hasn't risen overall in the last five years, suggesting it contains fundamental issues
    """
    if(direction == "above"):
        return False
    
    history = get_historicals(stockTicker, "day", "year", "regular")

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
    sma1 = ta.volatility.bollinger_mavg(price, int(n1), False)
    sma2 = ta.volatility.bollinger_mavg(price, int(n2), False)
    series = [price.rename("Price"), sma1.rename("Indicator1"), sma2.rename("Indicator2"), dates.rename("Dates")]
    df = pd.concat(series, axis=1)
    cross = get_last_crossing(df, days, symbol=stockTicker, direction=direction)
    
    if(cross) and plot:
        show_plot(price, sma1, sma2, dates, symbol=stockTicker, label1=str(n1)+" day SMA", label2=str(n2)+" day SMA")
    return cross


def stockhood_main(stockTicker, n1, n2, days, direction=""):
    """Determine if a golden/death cross has occured for a specified stock in the last X trading days

    Args:
        stockTicker(str): Symbol of the stock we're querying
        n1(int): Specifies the short-term indicator as an X-day moving average.
        n2(int): Specifies the long-term indicator as an X-day moving average.
                 (n1 should be smaller than n2 to produce meaningful results, e.g n1=50, n2=200)
        days(int): Specifies the maximum number of days that the cross can occur by
        direction(str): "above" if we are searching for an upwards cross, "below" if we are searching for a downwaords cross. Optional, used for printing purposes

    Returns:
        1 if the short-term indicator crosses above the long-term one
        0 if there is no cross between the indicators
        -1 if the short-term indicator crosses below the long-term one
        False if direction == "above" and five_year_check(stockTicker) returns False, meaning that we're considering whether to
            buy the stock but it hasn't risen overall in the last five years, suggesting it contains fundamental issues
    """
    if(direction == "above"):
        print("Direction Above!")
        return False
    
    history = get_historicals(stockTicker, "day", "year", "regular")

    #Couldn't get pricing data
    if(history is None or None in history):
        print("No History!")
        return False
    print('First')
    closingPrices = []
    dates = []
    print('Second')
    for item in history:
        closingPrices.append(float(item['close_price']))
        dates.append(item['begins_at'])
    price = pd.Series(closingPrices)
    dates = pd.Series(dates)
    dates = pd.to_datetime(dates)
    cross = 0
    print(stockTicker)
    print(price)
    print(dates)
    sma1 = ta.volatility.bollinger_mavg(price, int(n1), False)
    sma2 = ta.volatility.bollinger_mavg(price, int(n2), False)
    series = [price.rename("Price"), sma1.rename("Indicator1"), sma2.rename("Indicator2"), dates.rename("Dates")]
    df = pd.concat(series, axis=1)
    print('\nPercentage Change 253 Days:')
    if closingPrices[0] != 0:
        print((closingPrices[252] - closingPrices[0]) / closingPrices[0] * 100)
        print(closingPrices[252] - closingPrices[0])
        if ((closingPrices[252] - closingPrices[0]) / closingPrices[0] * 100) > 15.00:
            cross = ((closingPrices[252] - closingPrices[0]) / closingPrices[0] * 100)
            print('TAKE ME 253 Day Mover!\n') 
    else:
        print("Starting Close Price was 0.00\n")
    print('\nPercentage Change 30 Days:')
    if closingPrices[0] != 0:
        print((closingPrices[252] - closingPrices[222]) / closingPrices[222] * 100)
        print(closingPrices[252] - closingPrices[222])
        if ((closingPrices[252] - closingPrices[222]) / closingPrices[222] * 100) > 15.00:
            cross = ((closingPrices[252] - closingPrices[222]) / closingPrices[222] * 100)
            print('TAKE ME 30 Day MOVER!\n') 
    else:
        print("Starting Close Price was 0.00\n")   

    print('\nPercentage Change 15 Days:')
    if closingPrices[0] != 0:
        print((closingPrices[252] - closingPrices[237]) / closingPrices[237] * 100)
        print(closingPrices[252] - closingPrices[237])
        if ((closingPrices[252] - closingPrices[237]) / closingPrices[237] * 100) > 15.00:
            cross = ((closingPrices[252] - closingPrices[237]) / closingPrices[237] * 100)
            print('TAKE ME 15 Day MOVER!\n') 
    else:
        print("Starting Close Price was 0.00\n")       

    print('\nPercentage Change 7 Days:')
    if closingPrices[0] != 0:
        print((closingPrices[252] - closingPrices[245]) / closingPrices[245] * 100)
        print(closingPrices[252] - closingPrices[245])
        if ((closingPrices[252] - closingPrices[245]) / closingPrices[245] * 100) > 15.00:
            cross = ((closingPrices[252] - closingPrices[245]) / closingPrices[245] * 100)
            print('TAKE ME 7 Day MOVER!\n') 
    else:
        print("Starting Close Price was 0.00\n")    

    print('\nPercentage Change 3 Days:')
    if closingPrices[0] != 0:
        print((closingPrices[252] - closingPrices[249]) / closingPrices[249] * 100)
        print(closingPrices[252] - closingPrices[249])
        if ((closingPrices[252] - closingPrices[249]) / closingPrices[249] * 100) > 15.00:
            cross = ((closingPrices[252] - closingPrices[249]) / closingPrices[249] * 100)
            print('TAKE ME 3 Day MOVER!\n') 
    else:
        print("Starting Close Price was 0.00\n")            

    print('Third')
    return cross

def stockhood_main2(stockTicker, intervals, upPerc, downPerc):
    """
    This will take into account how far you would like to go in 5 minute intervals starting from the latest 5 minute candle
    """  
    try:
        history = get_historicals(stockTicker, "5minute", "day", "regular")
    except:
        print('This is the Exception')
    #Couldn't get pricing data
    if(history is None or None in history):
        return False
    closingPrices = []
    dates = []
    for item in history:
        closingPrices.append(float(item['close_price']))
        dates.append(item['begins_at'])

    num = len(closingPrices)

    #Positive?
    if closingPrices[0] != 0:
        if ((closingPrices[num - 1] - closingPrices[num - (int(intervals) + 1)]) / closingPrices[num - (int(intervals) + 1)] * 100) > float(upPerc):
            print((closingPrices[num - 1] - closingPrices[num - (int(intervals) + 1)]) / closingPrices[num - (int(intervals) + 1)] * 100)
            print(stockTicker)
            print('+++This Stock is Rising Fast!+++\n') 

    #Negative?
    if closingPrices[0] != 0:
        if (((closingPrices[num - 1] - closingPrices[num - int(intervals)]) / closingPrices[num - int(intervals)] * 100) < (0 - float(downPerc))):
            print((closingPrices[num - 1] - closingPrices[num - int(intervals)]) / closingPrices[num - int(intervals)] * 100)
            print(stockTicker)
            print('---Drop Alert!---\n') 



def stockhood_goldencross(stockTicker, n1, n2, days, direction=""):
    """
    Determine if a golden/death cross has occured for a specified stock in the last X trading days
    Args:
        stockTicker(str): Symbol of the stock we're querying
        n1(int): Specifies the short-term indicator as an X-day moving average.
        n2(int): Specifies the long-term indicator as an X-day moving average.
                 (n1 should be smaller than n2 to produce meaningful results, e.g n1=50, n2=200)
        days(int): Specifies the maximum number of days that the cross can occur by
        direction(str): "above" if we are searching for an upwards cross, "below" if we are searching for a downwards cross. Optional, used for printing purposes
    Returns:
        1 if the short-term indicator crosses above the long-term one
        0 if there is no cross between the indicators
        -1 if the short-term indicator crosses below the long-term one
        False if direction == "above" and five_year_check(stockTicker) returns False, meaning that we're considering whether to
        buy the stock but it hasn't risen overall in the last five years, suggesting it contains fundamental issues.
    """
    
    history = get_historicals(stockTicker, "day", "year", "regular")

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
    sma1 = ta.volatility.bollinger_mavg(price, int(n1), False)
    sma2 = ta.volatility.bollinger_mavg(price, int(n2), False)
    series = [price.rename("Price"), sma1.rename("Indicator1"), sma2.rename("Indicator2"), dates.rename("Dates")]
    df = pd.concat(series, axis=1)
    cross = get_last_crossing(df, days, symbol=stockTicker, direction=direction)
    

    show_plot(price, sma1, sma2, dates, symbol=stockTicker, label1=str(n1)+" day SMA", label2=str(n2)+" day SMA")
    return cross

def sell_holdings(symbol, holdings_data):
    """ Place an order to sell all holdings of a stock.

    Args:
        symbol(str): Symbol of the stock we want to sell
        holdings_data(dict): dict obtained from get_modified_holdings() method
    """
    shares_owned = int(float(holdings_data[symbol].get("quantity")))
    if not debug:
        r.order_sell_market(symbol, shares_owned)
    print("####### Selling " + str(shares_owned) + " shares of " + symbol + " #######")

def buy_holdings(potential_buys, profile_data, holdings_data):
    """ Places orders to buy holdings of stocks. This method will try to order
        an appropriate amount of shares such that your holdings of the stock will
        roughly match the average for the rest of your portfoilio. If the share
        price is too high considering the rest of your holdings and the amount of
        buying power in your account, it will not order any shares.

    Args:
        potential_buys(list): List of strings, the strings are the symbols of stocks we want to buy
        symbol(str): Symbol of the stock we want to sell
        holdings_data(dict): dict obtained from r.build_holdings() or get_modified_holdings() method
    """
    cash = float(profile_data.get('cash'))
    portfolio_value = float(profile_data.get('equity')) - cash
    ideal_position_size = (safe_division(portfolio_value, len(holdings_data))+cash/len(potential_buys))/(2 * len(potential_buys))
    prices = r.get_latest_price(potential_buys)
    for i in range(0, len(potential_buys)):
        stock_price = float(prices[i])
        if(ideal_position_size < stock_price < ideal_position_size*1.5):
            num_shares = int(ideal_position_size*1.5/stock_price)
        elif (stock_price < ideal_position_size):
            num_shares = int(ideal_position_size/stock_price)
        else:
            print("####### Tried buying shares of " + potential_buys[i] + ", but not enough buying power to do so#######")
            break
        print("####### Buying " + str(num_shares) + " shares of " + potential_buys[i] + " #######")
        if not debug:
            r.order_buy_market(potential_buys[i], num_shares)

def timeseriesmomentummeanreversion(stockTicker):
    history = get_historicals(stockTicker, "day", "5year", "regular")

    #Couldn't get pricing data
    if(history is None or None in history):
        return False
    #Populate a DataFrame
    stockprices = pd.DataFrame.from_dict(history)

    #Add a 20D Mean Column to our DataFrame
    stockprices['SMA'] = stockprices['close_price'].rolling(20).mean()
    #We calculate our extension to see whether a movement is over/under extended by calculating the move as a percentage of our SMA indicator.
    stockprices['extension'] = (stockprices['close_price'].astype(float) - stockprices['SMA'].astype(float)) / stockprices['SMA'].astype(float)
    #Calculate the difference between the closing price for each of the days, and the 20 day moving average
    stockprices['difference'] = stockprices['close_price'].astype(float) - stockprices['SMA'].astype(float)
    #Calculate return percentage
    stockprices['return'] = stockprices['close_price'].astype(float) / stockprices['close_price'].shift(1).astype(float)
    #Add long column which will display whether or not we should take a position at this time. 1 = Go Long \ NaN = Do not act
    stockprices['long'] = np.where(stockprices['difference'] < -2 ,1,np.nan)
    #Multiply the difference of the current day with the previous day difference. This will let us see when the close prices
    #crosses above the 20 day moving average since then there will be a change of sign. If this is the case, we will then hold the position. 
    #This is indicated by a 0 in the long column.
    stockprices['long'] = np.where(stockprices['difference'] * stockprices['difference'].shift(1) < 0, 0, stockprices['long'])
    #We use ffill pandas method in order to replace Nan with 0, indicating that in these days we hold our position.
    stockprices['long'] = stockprices['long'].ffill().fillna(0)
    #Multiply yesterdays long value by the return to find out if indeed there was a profit or loss made in connection with the stock.
    stockprices['gain_loss'] = stockprices['long'].shift(1) * stockprices['return']
    #Remove missing values for SMA Column.
    stockprices = stockprices.dropna(subset=['SMA'])
    #Total of Gain Loss Column
    stockprices['total'] =  stockprices['gain_loss'].cumsum()
    print("Should I Buy?")
    print(stockprices.tail(30))



def SMAMeanReversion():
    ticker = "AMC"
    sma = 50
    threshold = 0.1
    shorts=True

    history = get_historicals(ticker, "day", "5year", "regular")

    #Couldn't get pricing data
    if(history is None or None in history):
        return False

    data = pd.DataFrame.from_dict(history)
    print(data)
    data['SMA'] = data['close_price'].rolling(sma).mean()
    data['extension'] = (data['close_price'].astype(float) - data['SMA'].astype(float)) / data['SMA'].astype(float)
    print(data)
    data['position'] = np.nan
    data['position'] = np.where(data['extension']<-threshold,1, data['position'])
    if shorts:
        data['position'] = np.where(data['extension']>threshold, -1, data['position'])
    print("1111")
    print(" ")
    print(data)
    data['position'] = np.where(np.abs(data['extension'].astype(float))<0.01,0, data['position'].astype(float))
    data['position'] = data['position'].ffill().fillna(0)
    
    # Calculate returns and statistics
    data['returns'] = data['close_price'].astype(float) / data['close_price'].shift(1).astype(float)
    data['log_returns'] = np.log(data['returns'])
    data['strat_returns'] = data['position'].shift(1).astype(float) * data['returns'].astype(float)
    data['strat_log_returns'] = data['position'].shift(1).astype(float) * data['log_returns'].astype(float)
    data['cum_returns'] = np.exp(data['log_returns'].cumsum())
    data['strat_cum_returns'] = np.exp(data['strat_log_returns'].cumsum())
    data['peak'] = data['cum_returns'].cummax()
    data['strat_peak'] = data['strat_cum_returns'].cummax()
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    fig, ax = plt.subplots(3, figsize=(10, 8), sharex=True)

    ax[1].plot(data['extension']*100, label='Extension', color=colors[0])
    ax[1].axhline(threshold*100, linestyle='--', color=colors[1])
    ax[1].axhline(-threshold*100, label='Threshold', linestyle='--', color=colors[1])
    ax[1].axhline(0, label='Neutral', linestyle=':', color='k')
    ax[1].set_title('Price Extension and Buy/Sell Thresholds')
    ax[1].set_ylabel(f'Extension (%)')
    ax[1].legend(bbox_to_anchor=[1, 0.75])
    ax[2].plot(data['position'])
    ax[2].set_xlabel('Date')
    ax[2].set_title('Position')
    ax[2].set_yticks([-1, 0, 1])
    ax[2].set_yticklabels(['Short', 'Neutral', 'Long'])
    plt.tight_layout()
    plt.show()


    print(data.dropna().tail(30))
    print(data['returns'])
    print(data['extension'].tail(30))
    return data.dropna()

def signal():
    ticker = "AMC"
    sma = 50
    threshold = 0.1
    shorts=True

    history = get_historicals(ticker, "day", "5year", "regular")

    #Couldn't get pricing data
    if(history is None or None in history):
        return False

    data = pd.DataFrame.from_dict(history)
    width = 0.0003 # 3 pips Gap example for Hourly OHLC data

    
    for i in range(len(data)):
        print(data)
        print(data.columns.values[i])
        print(data.loc[i])
        if (data['open_price'].loc[i] > data['close_price'].loc[i + 1]):
            if(data['open_price'].loc[i] - data['close_price'].loc[i + 1] >= width):
                if(data['low_price'].loc[i] <= data['close_price'].loc[i + 1]):
                    print('trigger')
                    data['buy'] = 1
            
        elif (data['open_price'].loc[i] < data['close_price'].loc[i + 1]): 
            if((data['open_price'].loc[i] - data['close_price'].loc[i + 1]).astype(float) >= width):
                if(data['high_price'].loc[i] >= data['close_price'].loc[i + 1]):
                    print('TESTINGG')
                    data['sell'] = -1
    
    print(data)        
    return data