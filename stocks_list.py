import yfinance
import bs4 as bs
import requests
from datetime import date, timedelta

from utility import *

###########################################################################
#                                                                         #
#       FUNCTIONS THAT HANDLE THE TXT FILE OF THE BASE STOCKS LIST        #
#                                                                         #
###########################################################################

def getTheStocksListFromFile():
    """A function that takes the list from the txt file and returns it
    as a python list of strings"""

    stocks_list_file = open("stocks_list.txt", "r")
    data = stocks_list_file.read()

    list_of_stocks = data.split("\n")

    stocks_list_file.close()

    return (list_of_stocks)

def upgradeTheStocksListFileBasedOnPrice(min_price=0, max_price=100):
    """This function will update the stocks_list.txt file to have stocks
    in it based on prices of the stocks.
    """
    print("Running Program\n")
    current_list_of_stocks = getTheStocksListFromFile()

    updated_list_of_stocks = []

    end_date = end_date = date.today()

    # If the end date falls on Sunday or Monday, it will be moved
    # to Saturday, which is a day this program can run on
    end_date = updateEndDate(end_date)
    start_date = end_date - timedelta(days=1)

    print("Updating the stocks list - This can take some time...\n")

    # Takes the close price value of a stock (of the last day) and compares
    # it to the prices that are given.
    # If the close price is between these two values, the stock is appended
    # into the updated list
    for stock in current_list_of_stocks:
        print("HERE1")
        last_day_candle_data = yfinance.download(stock, start_date, end_date, progress=False)
        print("HERE2")
        close_price = float(last_day_candle_data['Close'])
        close_price = round(close_price, 2)
        if (min_price < close_price < max_price):
            print(stock, close_price)
            updated_list_of_stocks.append(stock)

    __replaceStocksInStocksListFile(updated_list_of_stocks)

    print("Finished updating the stock list in the file\n")

###########################################################################
#      ADDING DIFFERENT LISTS TO THE stocks_list.txt FILE FUNCTIONS       #
###########################################################################

# S&P 500
##########
def addingSandPStocksToTheFile():
    """A function that adds (or updates) the S&P 500 stocks list into the
    stocks_list.txt file
    """
    print("Running program")

    new_stocks_list = __getSandPStockListFromWeb()

    print("Adding S&P 500 stocks into the file")

    __addStocksToFile(new_stocks_list)

    print("Stocks added - You can look at the file")

# NASDAQ 100
#############
# def addingNASDAQOneHundredStocksToTheFile():
    



###########################################################################
#                          SUPPORTING FUNCTIONS                           #
###########################################################################

def __addStocksToFile(new_stocks_list):
    """A function that adds new stock names to the file, after it
    sorted them in assending order (A -> Z)"""

    # Get the stocks already in the file into a list
    list_of_stocks = getTheStocksListFromFile()

    stocks_list_file = open("stocks_list.txt", "w")

    # Append the new stocks from the new list into the existing list
    for stock in new_stocks_list:
        list_of_stocks.append(stock)

    # Get rid of duplicates
    list_of_stocks = list(dict.fromkeys(list_of_stocks))

    # Sort the appended list
    list_of_stocks.sort()

    # Write the sorted list into the txt file
    list_size = len(list_of_stocks)

    for i in range(list_size):
        stocks_list_file.write(list_of_stocks[i])
        stocks_list_file.write("\n")
    
    stocks_list_file.close()


def __replaceStocksInStocksListFile(new_stocks_list):
    """A function that replaces the list of stocks in the file with a
    new list of stocks and sorts them in assending order (A -> Z)
    """
    stocks_list_file = open("stocks_list.txt", "w")

    # Get rid of duplicates
    new_stocks_list = list(dict.fromkeys(new_stocks_list))

    # Sort the new list
    new_stocks_list.sort()

    # Write the sorted list into the txt file
    list_size = len(new_stocks_list)

    for i in range(list_size):
        stocks_list_file.write(new_stocks_list[i])
        stocks_list_file.write("\n")
    
    stocks_list_file.close()


def __getSandPStockListFromWeb():
    """This function gets the list of stocks in the S&P 500 , from the wikipedia
    web page and returns it as a list of tickers/symbols
    
    """

    # Getting the list from wikipedia and putting into a table
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    # Putting the info from the table into a list (Each ticker comes with \n at the
    # end, like - 'AAPL\n', so it needs to be removed)
    tickers = []

    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        ticker = ticker[:len(ticker)-1] # This line removes the \n at the end
        tickers.append(ticker)

    return (tickers)


def __sortTheTXTFileStocksList():
    """A function that sorts the list in the txt file in accending
    order (A -> Z)"""

    list_of_stocks = getTheStocksListFromFile()
    list_of_stocks.sort()

    list_size = len(list_of_stocks)

    stocks_list_file = open("stocks_list.txt", "w")

    for i in range(list_size):
        stocks_list_file.write(list_of_stocks[i])
        stocks_list_file.write("\n")
    
    stocks_list_file.close()

