###########################################################################
#                                                                         #
#         FUNCTIONS THAT HANDLE THE TXT FILE OF THE VALID STOCKS          #
#                                                                         #
###########################################################################

def updateValidStocksFile(valid_stocks_list):
    """A function that writes the valid stocks that were found into
    the valid_stocks_list.txt file
    """
    # Delete the list of stocks in the file
    valid_stocks_file = open("valid_stocks_list.txt", "w")
    valid_stocks_file.close()

    # Write the new list of stocks into the file
    valid_stocks_file = open("valid_stocks_list.txt", "a")

    for valid_stock in valid_stocks_list:
        valid_stocks_file.write(valid_stock)
        valid_stocks_file.write("\n")

    valid_stocks_file.close()


def updatedHorizontalStrategyStocksFile(valid_stocks_list):
    """A function that writes the valid stocks that were found into
    the horizontal_strategy_valid_stocks.txt file
    """
    # Delete the list of stocks in the file
    valid_stocks_file = open("horizontal_strategy_valid_stocks.txt", "w")
    valid_stocks_file.close()

    # Write the new list of stocks into the file
    valid_stocks_file = open("horizontal_strategy_valid_stocks.txt", "a")

    for valid_stock in valid_stocks_list:
        valid_stocks_file.write(valid_stock)
        valid_stocks_file.write("\n")

    valid_stocks_file.close()


def updateThreeCandlesStrategyStocksFile(valid_stocks_list):
    """A function that writes the valid stocks that were found into
    the three_candles_strategy_valid_stocks.txt file
    """
    # Delete the list of stocks in the file
    valid_stocks_file = open("three_candles_strategy_valid_stocks.txt", "w")
    valid_stocks_file.close()

    # Write the new list of stocks into the file
    valid_stocks_file = open("three_candles_strategy_valid_stocks.txt", "a")

    for valid_stock in valid_stocks_list:
        valid_stocks_file.write(valid_stock)
        valid_stocks_file.write("\n")

    valid_stocks_file.close()




# TO REMOVE??
# def __eraseValidStocksFileContent(valid_stocks_file):
#     """A function that erases the content inside the valid_stocks.txt file.
#     """
#     valid_stocks_file = open("valid_stocks.txt", "w")
#     valid_stocks_file.close()