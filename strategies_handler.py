from tkinter import *

from stock import *
from stocks_list import *
from strategies import *


def mainStrategyHandler(strategy_data, stock_list_choices, stock_prices_data):
    stocks_list_file_name = "stocks_list.txt"

    __stockListsHandler(stock_list_choices)

    __strategyHandler(strategy_data, stock_prices_data, stocks_list_file_name)
    

###########################################################################
#                            MAIN HANDLERS                                #
###########################################################################

def __stockListsHandler(stock_list_choices):
    """This function adds the required stocks lists based on the
    choices of the user.
    """
    file_name = "stocks_list.txt"
    clearFile(file_name)

    list_of_functions = [
        addingTehcnologicGiantsStocksToTheFile,
        addingSandPStocksToTheFile,
        addingNASDAQOneHundredStocksToTheFile,
        addingRussellOneThousandStocksToTheFile,
        addingLeveragedLongStocksToTheFile
    ]

    list_size = len(stock_list_choices)

    # If the choice is TRUE it will run the appropriate function
    for i in range(list_size):
        if (True == stock_list_choices[i]):
            list_of_functions[i](file_name)

    
def __strategyHandler(strategy_data, stock_prices_data, stocks_list_file_name):

    """This function will activate the right strategy function based
    on the choice of the user.
    """
    strategy_name = strategy_data["strategy_name"]
    number_of_days = strategy_data["number_of_days"]
    end_date = strategy_data["end_date"]

    min_price = stock_prices_data["minimum_price"]
    max_price = stock_prices_data["maximum_price"]

    final_stocks_list = []

    print("\n")
    print(strategy_name, " STRATEGY")
    print("---------------------------------\n")
          
    print("Running the program\n")
    first_stocks_list = __createStocks(stocks_list_file_name)

    print("Creating Candles (Will take some time)...\n")
    final_stocks_list = __createStockCandles(first_stocks_list,
                            number_of_days, end_date, min_price, max_price)

    # __printStocksCandles(final_stocks_list, number_of_days)

    # ACTIVATING THE RIGHT STRATEGY ACCORDING TO THE USER CHOICE
    index = strategy_data["strategy_num"]

    list_of_functions = [
        threeCandlesStrategy,
        horizontalStrategy
        ]
    
    list_of_functions[index](final_stocks_list, number_of_days)


###########################################################################
#                         SUPPORTING FUNCTIONS                            #
###########################################################################

def __createStocks(file_name):
    """A function that returns a list of objects of type Stock.
    This list is based on the list of stocks that exist in the txt file
    """

    # Get the list of stocks names from the txt file
    # stocks_names_list = getTheStocksListFromFile()
    stocks_names_list = getFileData(file_name)

    list_size = len(stocks_names_list)

    stocks_list = []

    # Create Stock objects and append them to one list
    for i in range(list_size):
        if (stocks_names_list[i] == ""):
            continue
        new_stock = Stock(stocks_names_list[i])
        stocks_list.append(new_stock)

    return (stocks_list)


def __createStockCandles(stocks_list, number_of_days, end_date, min_price, max_price):
    """A function that creates candles, from today backward, in all
    the stocks that are in the given list.
    The function will create the right candles in a stock and then move on
    to the next stock to do the same for that.
    """
    updated_stock_list = []

    # FOR PRACTICE
    # end_date = date.today() - timedelta(days=49)
    # print(end_date)

    # Creates the candles for each stock inside the given list
    for stock in stocks_list:
        status = stock.createCandels(end_date, number_of_days, min_price, max_price)
        if (status == True):
            updated_stock_list.append(stock)

    return (updated_stock_list)


def __printStocksCandles(stocks_list, number_of_days):
    """A function that prints out all the candles of all the stocks
    in the given list.
    """
    for stock in stocks_list:
        print("\n")
        print(stock.getSymbol())
        print("-------------\n")
        stock.printCandlesList(number_of_days)