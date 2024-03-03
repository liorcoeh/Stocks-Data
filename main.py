from tkinter import *
from mainWindow import *




root = Tk()

main_window = MainWindow(root)

main_window.setMainWindow()
main_window.createButtons()


root.mainloop()





#  **************    TO REMOVE   *******************

# from datetime import date, timedelta
# from stock import *
# from stocks_list import *

# from horizontal_strategy import *
# from three_candles_strategy import *

###########################################################################
#      UPDATING THE stocks_list.txt FILE - SHOULD DO ONCE A WEEK?         #
###########################################################################

# addingLeveragedLongStocksToTheFile()

# addingSandPStocksToTheFile()

# upgradeTheStocksListFileBasedOnPrice()

###########################################################################
#               THE REAL PROGRAM - DIFFERENT STRATEGIES                   #
###########################################################################


# horizontalStrategyFunc()

# threeCandlesStrategy()

