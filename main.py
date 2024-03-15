from tkinter import *
from mainWindow import *

from stocks_list import *


root = Tk()

main_window = MainWindow(root)

main_window.setMainWindow()
main_window.createButtons()


root.mainloop()

# file_name = "stocks_list.txt"
# clearFile(file_name)
# addingTehcnologicGiantsStocksToTheFile(file_name)
