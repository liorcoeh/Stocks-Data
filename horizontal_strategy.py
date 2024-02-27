
"""
This file is the main file for the HORIZONTAL STRATEGY
This startegy gets amount of days and returns the names of the stocks
which have candles during those days at a horizontal level.
Meaning, in this span of time there was no up or down in the stock.

This strategy works in this way:
1) It gets the required days from the user - if nothing is put,
   the default is 7.
2) It gets the date to count back from - if nothing is put, the
   default is today's date (The date when the program runs).
3) It creates a list of stocks, based on the stocks_list.txt file.
4) It creates the candles for each stock (based on the amount of days
   and the date that were taken from the user.)
5) From the first two candles (The two most earlier dates) it takes the
   highest high-price (between the two candles) and the lowest low-price
   (between the two candles). These two values will determine the range
   in which the following candles must be inside of.
6) Checks all the candles in each stock, if they are withing the range
   that was determined in the previous clause.
"""
from stock import *
from stocks_list import *
from valid_stocks import *

from datetime import datetime


def horizontalStrategyFunc():
    print("Hello and welcome to the HORIZONATL STRATEGY")
    print("--------------------------------------------\n")

    number_of_days = __getUserNumberOfDays()
    if (number_of_days == -1):
        print("Exisiting the program, GoodBye\n")
        return (False)

    end_date = __getUserDate()

    print("Creating Stocks\n")
    stocks_list = __createStocks()

    print("Creating Candles (Will take some time)...\n")
    __createAllCandles(stocks_list, end_date, number_of_days)

    # __printStocksCandles(stocks_list, number_of_days)

    print("Getting the valid Stocks\n")
    __checkHorizontalStrategy(stocks_list, number_of_days)

    print("The program is finished, you can open the horizontal_strategy_valid_stocks.txt file\n\n")


    ##########################################################################################
    #########                            SELF FUNCTIONS                              #########
    ##########################################################################################


##########################################################################################
#########                          SUPPORT FUNCTIONS                             #########
##########################################################################################

def __getUserNumberOfDays():
    """A function to get the number of days from the user. This number
    will decide how many candels will be created.
    If the user doesn't give a number it will be set to 7
    """

    print("Please enter the number of days to run the strategy on (must be 2 or more)")
    print("If you will just press Enter it will be 7 days")

    number_of_days = input()

    if (number_of_days == ""):  # If Enter was pressed
        number_of_days = 7
    else:
        number_of_days = int(number_of_days)
        if (number_of_days < 2):
            print("\nThe number of days must be 2 or more\n")
            return (-1)

    print("\n")

    return (number_of_days)


def __getUserDate():
    """A function that gets a date from the user.
    The user must give the date in the format: YYYY-MM-DD
    If the user doesn't give a date, it will be set to today's date.
    """

    print("Please enter the date you want to go back from (YYYY-MM-DD)")
    print("If you will enter nothing (press Enter) the date will be TODAY")

    end_date = input()

    if (end_date == ""):  # If Enter was pressed
        end_date = date.today()
    else:
        # Change the input from string to datetime.date
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # Omit the Hours, Minutes and Seconds from the datetime.date
        end_date = end_date.date()

    print("\n")

    return (end_date)


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
        if stocks_names_list[i] is "":
            continue
        new_stock = Stock(stocks_names_list[i])
        stocks_list.append(new_stock)

    return (stocks_list)


def __createAllCandles(stocks_list, end_date, number_of_days):
    """A function that creates the right amount of candles, in the specific
    requested time, in all the stocks that are in the given list.
    The function will create the right candles in a stock and then move on
    to the next stock to do the same for that.
    """

    # Creates the candles for each stock inside the given list
    for stock in stocks_list:
        print("starting {stock}".format(stock=stock.getSymbol()))
        stock.createCandels(end_date, number_of_days)


def __printStocksCandles(stocks_list, number_of_days):
    for stock in stocks_list:
        print("\n")
        print(stock.getSymbol())
        print("-------------\n")
        stock.printCandlesList(number_of_days)


##########################################################################################
#########             THE HORIZONTAL STRATEGY SUPPORT FUNCTIONS                  #########
##########################################################################################

def __checkHorizontalStrategy(stocks_list, number_of_days):
    """A function that checks if the candles of a specific stock are valid candles
    under the Horizontal Strategy and if it is a valid one, puts it into the 
    horizontal_strategy_valid_stocks.txt file
    """

    valid_stocks_list = []

    for stock in stocks_list:
        if (__checkStockCandlesInBounds(stock, number_of_days) == True):
            valid_stocks_list.append(stock.getSymbol())

    updatedHorizontalStrategyStocksFile(valid_stocks_list)


def __checkStockCandlesInBounds(stock, number_of_days):
    """This function checks if the candles inside the given stock are
    within the right range of the HORIZONATL STRATEGY
    """
    candles_list = stock.getCandlesList()

    if (__validRange(candles_list, number_of_days) == False):
            return (False)

    the_wanted_low_price = __getTheWantedLowPrice(candles_list, number_of_days)
    the_wanted_high_price = __getTheWantedHighPrice(candles_list, number_of_days)

    # TO REMOVE
    # print("Stock Symbol: ", stock.getSymbol())
    # print("Referance Low: ", the_wanted_low_price)
    # print("Referance High: ", the_wanted_high_price)

    for candle in candles_list:
        candle_low_price = candle.getLow()
        candle_high_price = candle.getHigh()

        if ((candle_low_price < the_wanted_low_price) or (candle_high_price > the_wanted_high_price)):
            # TO REMOVE
            # print("New Low:", candle_low_price)
            # print("New High:", candle_high_price)
            # print()
            return (False)
    
    return (True)


def __validRange(candles_list, number_of_days):
    """This function checks if the range of the HORIZONATL STRATEGY is
    even valid:
    If the first candle is higher than the second one, it must check
    that the first low-price isn't higher than the second high-price.
    If the first candle is lower than the second on, it much check that
    the first high-price isn't lower than the second low-price.
    """
    last_candle_num = number_of_days - 1
    pre_last_candle_num = number_of_days - 2

    last_candle_high_price = candles_list[last_candle_num].getHigh()
    last_candle_low_price = candles_list[last_candle_num].getLow()

    pre_last_candle_high_price = candles_list[pre_last_candle_num].getHigh()
    pre_last_candle_low_price = candles_list[pre_last_candle_num].getLow()

    if (last_candle_low_price > pre_last_candle_high_price or
                        last_candle_high_price < pre_last_candle_low_price):
        # TO REMOVE
        # print("Last and Pre-Last candles are with a gap")
        return (False)
    
    return (True)
        

def __getTheWantedHighPrice(candles_list, number_of_days):
    """This function looks at the two most earlier (by date) candles (they
    are the last two candles in the list) and takes the higher 'high price'
    between these two.
    This high price will be used to compare all the rest of the high prices of
    the rest of the candles.
    """
    last_candle_num = number_of_days - 1
    pre_last_candle_num = number_of_days - 2

    last_candle_high_price = candles_list[last_candle_num].getHigh()

    pre_last_candle_high_price = candles_list[pre_last_candle_num].getHigh()

    # TO REMOVE
    # print(last_candle_high_price)
    # print(pre_last_candle_high_price)
    # print()

    if (last_candle_high_price > pre_last_candle_high_price):
        return (last_candle_high_price)
    
    return (pre_last_candle_high_price)
        

def __getTheWantedLowPrice(candles_list, number_of_days):
    """This function looks at the two most earlier (by date) candles (they
    are the last two candles in the list) and takes the lower 'low price'
    between these two.
    This low price will be used to compare all the rest of the low prices of
    the rest of the candles.
    """
    last_candle_num = number_of_days - 1
    pre_last_candle_num = number_of_days - 2

    last_candle_low_price = candles_list[last_candle_num].getLow()

    pre_last_candle_low_price = candles_list[pre_last_candle_num].getLow()

    # TO REMOVE
    # print(last_candle_low_price)
    # print(pre_last_candle_low_price)
    # print()

    if (last_candle_low_price < pre_last_candle_low_price):
        return (last_candle_low_price)
    
    return (pre_last_candle_low_price)