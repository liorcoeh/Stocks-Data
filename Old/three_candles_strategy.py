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


def threeCandlesStrategy(stocks_list, number_of_days):

    print("Checking the THREE CANDLES strategy\n")
    
    __checkThreeCandlesStrategy(stocks_list, number_of_days)

    print("The program is finished, you can open the valid_stocks_list.txt file\n\n")


###########################################################################
#                         SUPPORTING FUNCTIONS                            #
###########################################################################

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

