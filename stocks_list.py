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


def clearFile(file_name):
    """A function that removes all the current information that is inside
    a given txt file.
    """
    txt_file = open(file_name, "w")
    txt_file.close()


def getFileData(file_name):
    """A function that takes the data (a list) from the txt file and returns
    it as a python list of strings.
    """
    txt_file = open(file_name, "r")

    data = txt_file.read()

    new_list = data.split("\n")

    txt_file.close()

    return (new_list)


def addListToFile(file_name, list_to_add):
    """A function that add the given list to the given txt file.
    Any old data in the file will be deleted.
    """
    # Get rid of duplicates
    list_to_add = list(dict.fromkeys(list_to_add))

    # Removing stock names that are problematic
    __removeBadStocksNames(list_to_add)

    # Sort the list
    list_to_add.sort()

    # Write the sorted list into the txt file
    txt_file = open(file_name, "w")

    list_size = len(list_to_add)

    for i in range(list_size):
        txt_file.write(list_to_add[i])
        txt_file.write("\n")

    txt_file.close()


def concatListToFile(file_name, list_to_add):
    """A function that adds the given list to the given txt file while
    maintaining the old data in the given file.
    The exisiting data and the new data will be combined (No duplicates,
    no unvalid names and it will be sorted).
    """
    list_of_stocks = getFileData(file_name)

    # Append the new stocks from the new list into the existing list
    for stock in list_to_add:
        list_of_stocks.append(stock)

    addListToFile(file_name, list_of_stocks)


def __removeBadStocksNames(list_of_stocks):
    """This function removes from the list that is given bad stock names:
    Names that contain a '.'
    """
    for stock_name in list_of_stocks:
        if ('.' in stock_name):
            list_of_stocks.remove(stock_name)



###########################################################################
#      ADDING DIFFERENT LISTS TO THE stocks_list.txt FILE FUNCTIONS       #
###########################################################################

# BASIC STOCKS
###############
    
def addingBasicStocksToTheFile(file_name):
    """A function that adds some basic stocks into the stocks_list.txt
    file.
    """
    # print("ADDING BASIC STOCKS")

    print()
    print("ADDING BASIC STOCKS TO THE TXT FILE")
    print("-----------------------------------\n")

    # NEEDS TO ADD SOME MORE STOCKS TO THIS LIST
    basic_stocks_list = [
        "AAPL",
        "MSFT"
    ]

    print("Adding the stocks...\n")

    concatListToFile(file_name, basic_stocks_list)

    print("Stocks added - You can open the file\n\n")


# S&P 500
##########
def addingSandPStocksToTheFile(file_name):
    """A function that adds (or updates) the S&P 500 stocks list into the
    stocks_list.txt file
    """
    # print("ADDING S&P 500 STOCKS")

    print()
    print("ADDING S&P500 STOCKS TO THE TXT FILE")
    print("------------------------------------\n")

    new_stocks_list = __getSandPStockListFromWeb()

    print("Adding the stocks...\n")

    concatListToFile(file_name, new_stocks_list)

    print("Stocks added - You can open the file\n\n")


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


# NASDAQ 100
#############
def addingNASDAQOneHundredStocksToTheFile(file_name):
    print("ADDING NASDAQ 100 STOCKS")
    

# LEVERAGED LONG STOCKS
#######################
def addingLeveragedLongStocksToTheFile(file_name):
    """A function that adds the levereged long stocks into the
    stocks_list.txt file
    """
    # print("ADDING LEVERAGED STOCKS")

    print()
    print("ADDING LEVERAGED LONG STOCKS TO THE TXT FILE")
    print("--------------------------------------------\n")

    new_stocks_list = [
        "QQQ",
        "QLD",
        "TQQQ",
        "SPY",
        "SSO",
        "UPRO",
        "DIA",
        "BF.B"
        "DDM",
        "UDOW",
        "IWM",
        "UWM",
        "URTY",
        "SOXX",
        "SOXL",
    ]

    print("Adding the stocks...\n")

    concatListToFile(file_name, new_stocks_list)

    print("Stocks added - You can open the file\n\n")
    
