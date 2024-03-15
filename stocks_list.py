import pandas as pd

"""
This file handles with txt files - Inserting new data, replacing data and so on
"""

##########################################################################################
##########################################################################################
#########                                                                        #########
#########                 FUNCTIONS THAT DEAL WITH TXT FILES                     #########
#########                                                                        #########
##########################################################################################
##########################################################################################

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

    for i in range(list_size - 1):
        txt_file.write(list_to_add[i + 1])
        txt_file.write("\n")

    # txt_file.write(list_to_add[i])
    # txt_file.write("\n")

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



##########################################################################################
##########################################################################################
#########                                                                        #########
#########         ADDING DIFFERENT LISTS TO THE THE GIVEN FILE FUNCTIONS         #########
#########                                                                        #########
##########################################################################################
##########################################################################################

            
##########################################################################################
#                             TECHNOLOGIC GIANTS STOCKS                                  #
##########################################################################################
    
def addingTehcnologicGiantsStocksToTheFile(file_name):
    """A function that adds some basic stocks into the stocks_list.txt
    file.
    """
    # print("ADDING BASIC STOCKS")

    print()
    print("ADDING TECHNOLOGIC GIANTS STOCKS TO THE TXT FILE")
    print("------------------------------------------------\n")

    # NEEDS TO ADD SOME MORE STOCKS TO THIS LIST
    technologic_giants_stocks_list = [
        "MSFT",
        "AAPL",
        "GOOG",
        "AMZN",
        "TSLA",
        "META",
        "NVDA",      
    ]

    print("Adding the TECHNOLOGIC GIANTS stocks...\n")

    concatListToFile(file_name, technologic_giants_stocks_list)

    print("Stocks added\n")


##########################################################################################
#                                   S&P 500 STOCKS                                       #
##########################################################################################

def addingSandPStocksToTheFile(file_name):
    """A function that adds the S&P 500 stocks list into the
    given txt file.
    """
    # print("ADDING S&P 500 STOCKS")

    print()
    print("ADDING S&P500 STOCKS TO THE TXT FILE")
    print("------------------------------------\n")

    new_stocks_list = __getSandPStockListFromWeb()

    print("Adding the S&P 500 stocks...\n")

    concatListToFile(file_name, new_stocks_list)

    print("Stocks added\n")


def __getSandPStockListFromWeb():
    """This function gets the list of stocks in the Nasdaq 100.
    It needs several important arguments to acheive this:
    1) html = http://en.wikipedia.org/wiki/List_of_S%26P_500_companies
       The url of the right wikipedia page.
    2) The table number out of all the tables on the wikipedia page
       The table number is 1.
    4) The header on the valid table to get the symbols from.
       The heaser is "Symbol"
    """
    table_num = 0
    
    s_and_p_500 = pd.read_html("http://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[table_num]
    s_and_p_500_symbols = s_and_p_500.Symbol.tolist()

    return (s_and_p_500_symbols)


##########################################################################################
#                                 NASDAQ 100 STOCKS                                      #
##########################################################################################

def addingNASDAQOneHundredStocksToTheFile(file_name):
    """A function that adds the Nasdaq 100 stocks list into the
    given txt file.
    """
    print()
    print("ADDING NASDAQ 100 STOCKS")
    print("------------------------\n")

    new_stocks_list = __getNasdaqOneHundredListFromWeb()

    print("Adding the NASDAQ 100 stocks...\n")

    concatListToFile(file_name, new_stocks_list)

    print("Stocks added\n")
    

def __getNasdaqOneHundredListFromWeb():
    """This function gets the list of stocks in the Nasdaq 100.
    It needs several important arguments to acheive this:
    1) html = https://en.wikipedia.org/wiki/Nasdaq-100
       The url of the right wikipedia page.
    2) The table number out of all the tables on the wikipedia page
       The table number is 4.
    4) The header on the valid table to get the symbols from.
       The header is "Ticker"
    """
    table_num = 4
    
    nasdaq_100 = pd.read_html("https://en.wikipedia.org/wiki/Nasdaq-100")[table_num]
    nasdaq_100_symbols = nasdaq_100.Ticker.tolist()

    return (nasdaq_100_symbols)


##########################################################################################
#                                RUSSELL 1000 STOCKS                                     #
##########################################################################################

def addingRussellOneThousandStocksToTheFile(file_name):
    """A function that adds the Russell 1000 stocks list into the
    given txt file.
    """
    print()
    print("ADDING RUSSELL 1000 STOCKS")
    print("--------------------------\n")

    new_stocks_list = __getRussellOneThousandListFromWeb()

    print("Adding the RUSSELL 1000 stocks...\n")

    concatListToFile(file_name, new_stocks_list)

    print("Stocks added\n")
    

def __getRussellOneThousandListFromWeb():
    """This function gets the list of stocks in the Russell 1000.
    It needs several important arguments to acheive this:
    1) html = https://en.wikipedia.org/wiki/Russell_1000_Index
       The url of the right wikipedia page.
    2) The table number out of all the tables on the wikipedia page
       The table number is 2.
    4) The header on the valid table to get the symbols from.
       The header is "Ticker"
    """
    table_num = 2
    
    nasdaq_100 = pd.read_html("https://en.wikipedia.org/wiki/Russell_1000_Index")[table_num]
    nasdaq_100_symbols = nasdaq_100.Ticker.tolist()

    return (nasdaq_100_symbols)



##########################################################################################
#                               LEVERAGED LONG STOCKS                                    #
##########################################################################################

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

    print("Adding the LEVERAGED stocks...\n")

    concatListToFile(file_name, new_stocks_list)

    print("Stocks added\n")
    
