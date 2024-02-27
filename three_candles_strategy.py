"""
This file is the main file for the THREE CANDLES STRATEGY
This strategy finds stocks in which 3 days in a row it was in downward
direction, meaning that each day was lower than the previous one.

This strategy wordk in this way:
1) It craetes a list of stocks, based on the stocks_list.txt file.
2) It creates the candles for each stock, 3 candles for each stock.
3) It compares the highes and lows of each candle with the one before it
   (before it, means by date).
4) If the candles are meeting the condition the stock will be sent out.
"""

from stock import *
from stocks_list import *
from valid_stocks import *

def threeCandlesStrategy():
    print("Hello and welcome to the THREE CANDLES STRATEGY")
    print("-----------------------------------------------\n")

    print("Running the program\n")
    
    print("Creating Stocks\n")
    stocks_list = __createStocks()

    print("Creating Candles (Will take some time)...\n")
    number_of_days = 3
    __createStockCandles(stocks_list, number_of_days)

    # __printStocksCandles(stocks_list, number_of_days)

    print("Getting the valid Stocks\n")
    __checkThreeCandlesStrategy(stocks_list, number_of_days)

    print("The program is finished, you can open the three_candles_strategy_valid_stocks.txt file\n\n")


def __createStocks():
    """A function that returns a list of objects of type Stock.
    This list is based on the list of stocks that exist in the txt file
    """

    # Get the list of stocks names from the txt file
    stocks_names_list = getTheStocksListFromFile()

    list_size = len(stocks_names_list)

    stocks_list = []

    # Create Stock objects and append them to one list
    for i in range(list_size):
        new_stock = Stock(stocks_names_list[i])
        stocks_list.append(new_stock)

    return (stocks_list)


def __createStockCandles(stocks_list, number_of_days):
    """A function that creates candles, from today backward, in all
    the stocks that are in the given list.
    The function will create the right candles in a stock and then move on
    to the next stock to do the same for that.
    """
    end_date = date.today()
    # FOR PRACTICE
    # end_date = date.today() - timedelta(days=49)
    # print(end_date)

    # Creates the candles for each stock inside the given list
    for stock in stocks_list:
        stock.createCandels(end_date, number_of_days)


def __printStocksCandles(stocks_list, number_of_days):

    for stock in stocks_list:
        print("\n")
        print(stock.getSymbol())
        print("-------------\n")
        stock.printCandlesList(number_of_days)



def __checkThreeCandlesStrategy(stocks_list, number_of_days):
    """A function that checks if the candles of a specific stock are valid candles
    under the Three Candles Strategy and if it is a valid one, puts it into the 
    three_candles_strategy_valid_stocks.txt file
    """

    valid_stocks_list = []

    for stock in stocks_list:
        if (__checkStockCandles(stock, number_of_days) == True):
            valid_stocks_list.append(stock.getSymbol())

    updateThreeCandlesStrategyStocksFile(valid_stocks_list)


def __checkStockCandles(stock, number_of_days):
    """This function checks if each candle is lower than the candle that
    came before it, there should be 3 candles in a dicending order.
    """
    candles_list = stock.getCandlesList()

    # Making sure the candles are in the right order (the older one based
    # on date, is the first candles)
    first_candle_num = number_of_days - 1
    second_candle_num = number_of_days - 2
    third_candle_num = number_of_days - 3

    # Taking the high and low prices of each of the candles
    first_candle_high_price = candles_list[first_candle_num].getHigh()
    first_candle_low_price = candles_list[first_candle_num].getLow()

    second_candle_high_price = candles_list[second_candle_num].getHigh()
    second_candle_low_price = candles_list[second_candle_num].getLow()

    third_candle_high_price = candles_list[third_candle_num].getHigh()
    third_candle_low_price = candles_list[third_candle_num].getLow()

    # Comparing the values of each candle, with the one before it
    if (first_candle_high_price < second_candle_high_price):
        return (False)
    
    if (first_candle_low_price < second_candle_low_price):
        return (False)
    
    if (second_candle_high_price < third_candle_high_price):
        return (False)
    
    if (second_candle_low_price < third_candle_low_price):
        return (False)
    
    return (True)