"""
This file is the file that holds all the different strategies that might be used.
"""

from stock import *
from stocks_list import *


##########################################################################################
##########################################################################################
#########                                                                        #########
#########                     THE THREE CANDLES STRATEGY                         #########
#########                                                                        #########
##########################################################################################
##########################################################################################

def threeCandlesStrategy(stocks_list, number_of_days):

    print("Checking the THREE CANDLES strategy\n")
    
    __checkThreeCandlesStrategy(stocks_list, number_of_days)

    print("The program is finished, you can open the valid_stocks_list.txt file\n\n")


##########################################################################################
#########                        SUPPORTING FUNCTIONS                            #########
##########################################################################################

def __checkThreeCandlesStrategy(stocks_list, number_of_days):
    """A function that checks if the candles of a specific stock are valid candles
    under the Three Candles Strategy and if it is a valid one, puts it into the 
    three_candles_strategy_valid_stocks.txt file
    """
    valid_stocks_list = []

    for stock in stocks_list:
        if (__checkStockCandles(stock, number_of_days) == True):
            valid_stocks_list.append(stock.getSymbol())

    # update the valid stocks list txt file
    valid_stocks_list_file_name = "valid_stocks_list.txt"
    addListToFile(valid_stocks_list_file_name, valid_stocks_list)


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



##########################################################################################
##########################################################################################
#########                                                                        #########
#########                       THE HORIZONTAL STRATEGY                          #########
#########                                                                        #########
##########################################################################################
##########################################################################################

def horizontalStrategy(stocks_list, number_of_days):
    
    print("checking the HORIZONTAL strategy\n")

    __checkHorizontalStrategy(stocks_list, number_of_days)

    print("The program is finished, you can open the valid_stocks_list.txt file\n\n")


##########################################################################################
#########                        SUPPORTING FUNCTIONS                            #########
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

    # update the valid stocks list txt file
    valid_stocks_list_file_name = "valid_stocks_list.txt"
    addListToFile(valid_stocks_list_file_name, valid_stocks_list)


def __checkStockCandlesInBounds(stock, number_of_days):
    """This function checks if the candles inside the given stock are
    within the right range of the HORIZONATL STRATEGY
    """
    candles_list = stock.getCandlesList()

    if (__validRange(candles_list, number_of_days) == False):
            return (False)

    the_wanted_low_price = __getTheWantedLowPrice(candles_list, number_of_days)
    the_wanted_high_price = __getTheWantedHighPrice(candles_list, number_of_days)

    for candle in candles_list:
        candle_low_price = candle.getLow()
        candle_high_price = candle.getHigh()

        if ((candle_low_price < the_wanted_low_price) or (candle_high_price > the_wanted_high_price)):
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

    if (last_candle_low_price < pre_last_candle_low_price):
        return (last_candle_low_price)
    
    return (pre_last_candle_low_price)

