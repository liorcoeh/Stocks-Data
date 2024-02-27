import yfinance
from datetime import timedelta

from candle import *
from utility import *

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning) # Ignores a warning about using float

import sys

class Stock:
    """A class that creates a 'Stock' in order to be able to have all
    the information about it at one place.
    """
    __stock_symbol = 0
    __candles_list = []
    __number_of_candles = 0

    def __init__(self, new_stock_symbol):
        """Initializes a new stock
        
        Parameters
        ----------
        new_stock_symbol : str, the stock symbol to be used, for example:
        Apple stock => 'AAPL'
        Amazon stock => 'AMZN'
        """

        self.__stock_symbol = new_stock_symbol


##########################################################################################
#########                      PUBLIC / GENERAL FUNCTIONS                        #########
##########################################################################################

    def getSymbol(self):
        """Returns the symbol of this stock.
        """
        return (self.__stock_symbol)


    def createCandels(self, end_date, number_of_days):
        """Creates a list of candles (of the last active days), depends on
        the number of days that are given.

        Parameters
        ----------
        end_date : Object of type - datetime.date
                   This is the date to count back from, meaning it will go back from
                   this date (it will not include this date) to create the list of
                   the candles.
        number_of_days : int - The number of days / candles to create
        """
        if (isDateValid(end_date) == False):
            print("Stock.py -> createCandles()")
            return (False)

        self.__number_of_candles = number_of_days

        # If the end date falls on Sunday or Monday, it will be moved
        # to Saturday, which is a day this program can run on
        end_date = updateEndDate(end_date)

        # At the moment there is no answer to the handling of running    #
        # it on Monday AFTER stock market hours. Also no holydays!!!     #
        ##################################################################
            
        start_date = end_date - timedelta(days=1)

        new_candles_list = []
        
        for day_num in range(self.__number_of_candles):
            print(end_date, start_date, day_num)
            new_candle = self.__createCandle(end_date, start_date, day_num + 1)

            new_candles_list.append(new_candle)

            end_date = end_date - timedelta(days=1)
            end_date = updateEndDate(end_date)

            start_date = end_date - timedelta(days=1)

        self.__candles_list = new_candles_list
    

    def getCandlesList(self):
        """A function that returns the list of candles inside
        this stock.
        """
        return(self.__candles_list)


    def printCandlesList(self, candles_num):
        """A function that prints the info inside each and every candle
        in the candles list of this stock.
        """
        for i in range(candles_num):
            self.__candles_list[i].printCandle()
            print("\n")


##########################################################################################
#########                       SUPPORTING FUNCTIONS                             #########
##########################################################################################

    def __createCandle(self, end_date, start_date, candle_number):
        """Creates an object of type Candle, that is based on given dates.
        These two dates will give the date of the candle:
        The start date is the actuall date to get the candle.
        The end date is the stop line to get the data (yfinace api)

        Parameters
        ----------
        end_date : Object of type - datetime.date
                   This is the date the candle ended before (one day before).
        start_date : Object of type - datetime.date
                     This is the requasted date of the candle.
        """
        flag = False

        # Getting the data from the web, using the yfinance api
        while (flag == False):
            try:
                candle_data = yfinance.download(self.__stock_symbol, start_date, end_date, progress=False)

                # Changing the data from string into floats - to be able to work on later
                stock_symbol = self.__stock_symbol
                serial_number = candle_number
                candle_date = str(start_date)
                open = float(candle_data['Open'])
                close = float(candle_data['Close'])
                high = float(candle_data['High'])
                low = float(candle_data['Low'])
                volume = float(candle_data['Volume'])

                # Rounding the floats we got - no need for more than 2 decimals
                open = round(open, 2)
                close = round(close, 2)
                high = round(high, 2)
                low = round(low, 2)
                volume = round(volume, 2)
                
                # Creating a candle using the data that was received
                new_candle = Candle(stock_symbol, serial_number, candle_date, 
                                                        open, close, high, low, volume)
                flag = True

            except:
                end_date = end_date - timedelta(days=1)
                start_date = start_date - timedelta(days=1)
        
        return (new_candle)


    
