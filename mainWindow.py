"""
This class is the class of the main window - The window that will pop up when activating
the entire program.
This class creates 4 types of buttons and puts the in the right location in the window.
1) The RUN button - The button that will activate the backend part of the program.
2) The STRATEGIES buttons - Buttons where one can chose what type of startegy he wants to run.
   Only one strategy can run at each time (The THREE CANDLES strategy is the default one).
3) The STOCK LISTS buttons - Buttons where one can chose what stocks he wants his strategy to
   run on. On can chose more than one list, therefore he can chose more than one button.
4) The STOCK PRICES buttons - Buttons where one can chose if he wants stocks in a range of
   prices to run the strategy on. Only one choice can be made (The no range is the default choice).

If you want to add new information to THIS file:
------------------------------------------------
ADDING A STRATEGY:
Add the name of the strategy to the self list - "__strategies_names".

ADDING A STOCKS LIST:
Add the name of the stocks list to the self list - "__stock_lists_names".

ADDING A STOCK PRICE RANGE (You shouldn't do that - cause they are all covered):
Add the name of the stock price to the self list - "__stock_prices_names".
"""

from tkinter import *
import datetime

from strategies_handler import *


class MainWindow:
    """A class that creates a "MainWindow" in order to run the program in it.
    """
    __root = ""

    # VARIABLES FOR THE STRATEGIES BUTTONS
    __strategies_names = [
        "THREE CANDLES",
        "HORIZONTAL"
    ]
    __strategies_buttons = []
    __strategy_data = {
        "strategy_name": "THREE CANDLES",
        "strategy_num": 0,
        "number_of_days": 3,
        "end_date": date.today()
    }
    
    __number_of_days = ""
    __end_date = ""


    # VARIABLES FOR THE STOCK LISTS BUTTONS
    __stock_lists_names = [
        "TECHNOLOGIC STOCKS",
        "S&P 500 STOCKS",
        "NASDAQ 100 STOCKS",
        "RUSSELL 1000 STOCKS",
        "LEVERAGED STOCKS"
    ]
    __stock_lists_buttons = []
    __stock_lists_choices = []

    # VARIABLES FOR THE STOCK PRICES BUTTONS
    __stock_prices_names = [
            "ALL PRICES",
            "FIXED PRICES",
            "USER PRICES"
        ]
    __stock_prices_buttons = []
    __stock_prices_data = {
        "name": "ALL PRICES",
        "minimum_price": 0,
        "maximum_price": 500000
    }

    __min_price = ""
    __max_price = ""


    # INITIALIZING THE MAIN WINDOW
    def __init__(self, root):
        """Initializes a new MainWindow.
        """
        self.__root = root


##########################################################################################
#                     THE MAIN FUNCTIONS OF THE MAIN WINDOW CLASS                        #
##########################################################################################

    def setMainWindow(self):
        """This function sets the Main Window:
        Colors
        Size
        Columns and Rows
        """
        self.__root.configure(bg="#020f12")

        window_width = self.__decide_window_width()
        window_height = self.__decide_window_height()

        x_position = self.__decide_window_horizontal_position()
        y_position = self.__decide_window_vertical_position()

        columns_amount = self.__get_column_amount()
        rows_amount = self.__get_row_amount()

        self.__root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        for i in range(columns_amount):
            self.__root.columnconfigure(i, weight=1, uniform='a')

        for i in range(rows_amount):
            self.__root.rowconfigure(i, weight=1, uniform='a')


    def createButtons(self):
        """This funtion creates all the necessary buttons to the main window.
        It is using supporting function for each button type.
        """
        self.__createRunButton()
        self.__createStrategiesButtons()
        self.__createStockListsButtons()
        self.__createStockPricesButtons()


##########################################################################################
#                  SETTING THE WINDOW SIZE AND POSISTION SELF FUNCTIONS                  #
##########################################################################################

    # GETTING THE PHYSICAL SCREEN'S SIZE
    def __get_screen_width(self):
        """A function that returns the widthe of the screen on which the program
        is running on, in pixles.
        """
        screen_width = self.__root.winfo_screenwidth()

        return (screen_width)

    def __get_screen_height(self):
        """A function that returns the height of the screen on which the program
        is running on, in pixels.
        """
        screen_height = self.__root.winfo_screenheight()

        return (screen_height)

    # CALCULATING THE PROGRAM WINDOW'S SIZE
    def __decide_window_width(self):
        """This function will fit the window to a standrad pc screen width of
        a 1920 pixels (or less, if the screen is smaller).
        """
        default_screen_width = 1920
        this_screen_width = self.__get_screen_width()

        if (this_screen_width > default_screen_width):
            return (default_screen_width)
        else:
            return (this_screen_width)

    def __decide_window_height(self):
        """This function will fit the window to a standrad pc screen height of
        a 1080 pixels (or less, if the screen is smaller).
        """
        default_screen_height = 1080
        this_screen_height = self.__get_screen_height()

        if (this_screen_height > default_screen_height):
            return (default_screen_height)
        else:
            return (this_screen_height)
    

    # CALCULATING THE POSTION OF THE PROGRAM'S WINDOW
    def __decide_window_horizontal_position(self):
        """This function will decided the horizontal position to put the
        window so it will appear at the middle of the screen.
        """
        this_screen_width = self.__get_screen_width()

        window_width = self.__decide_window_width()

        if (window_width < this_screen_width):
            x_position = (this_screen_width / 2) - (window_width / 2)
        else:
            x_position = 0

        # It must return an int cause that is what the functions use
        return (int(x_position))

    def __decide_window_vertical_position(self):
        """This function will decided the vertical position to put the
        window so it will appear at the middle of the screen.
        """
        this_screen_height = self.__get_screen_height()

        window_height = self.__decide_window_height()

        if (window_height < this_screen_height):
            y_position = (this_screen_height / 2) - (window_height / 2)
        else:
            y_position = 0

        # It must return an int cause that is what the functions use
        return (int(y_position))

    # CALCULATING THE NUMBER OF COLUMNS AND ROWS OF THE PROGRAM'S WINDOW
    def __get_column_amount(self):
        """This function sets how many columns the window of the program will have,
        it is based on the values that will be inside the window.
        """
        stocks_lists_column = 1
        stocks_prices_columns = 3
        strategy_columns = 2

        total_columns = stocks_lists_column + 1

        if (stocks_prices_columns >= strategy_columns):
            total_columns = total_columns + stocks_prices_columns
        else:
            total_columns = total_columns + strategy_columns
        
        total_columns = total_columns + 1

        return (total_columns)

    def __get_row_amount(self):
        """This function sets how many rows the window of the program will have,
        it is based on the number to stocks list that exists in the program.
        """
        min_row_num = 10
        stocks_list_num = 3

        if (stocks_list_num >= min_row_num):
            return (stocks_list_num)
        else:
            return (min_row_num)
        

##########################################################################################
#                          RUN BUTTON AND SUPPORTING FUNCTIONS                           #
##########################################################################################
        
    def __createRunButton(self):
        """This function creates the button for the run function.
        """

        blue = "#05d7ff"
        light_blue = "#65e7ff"
        light_green = "#65fff2"
        black = "BLACK"
        background_color = blue

        button_width = 20
        button_height = 2

        column_position = self.__get_column_amount() - 1
        row_position = self.__get_row_amount() - 2

        # Set the RUN button properties
        new_button = Button(self.__root,
                        command=lambda : self.__runProgram(),    
                        text="RUN",
                        font=("Raleway", 16, "bold"),                           
                        background=background_color,
                        foreground=black,
                        activebackground=light_blue,
                        activeforeground=black,
                        highlightthickness=2,
                        highlightbackground=blue,
                        highlightcolor="WHITE",
                        width=button_width,
                        height=button_height,
                        border=0,
                        cursor="hand1")

        # Position the RUN button on the main window grid
        new_button.grid(column=column_position, row=row_position)


    def __runProgram(self):
        """This function will run the backend program based on all the information
        that was received by the user.
        """
        print("RUNNING THE PROGRAM - NEEDS TO UPDATE THIS FUNCTION")
        
        mainStrategyHandler(self.__strategy_data,
                            self.__stock_lists_choices, self.__stock_prices_data)

        self.__validStocksWindow()


    def __validStocksWindow(self):
        print("**** FINISHED THE PROGRAM ****")

        stocks_window = Tk()
        stocks_window.title("The Valid Stocks")
        stocks_window.geometry("300x600+700+300")

        text_widget = Text(stocks_window, wrap="word", width=40, height=30)
        text_widget.pack(pady=10)

        content = self.__getStocksFromFile()
        text_widget.delete(1.0, END) # Clear previous content
        text_widget.insert(END, content)

    
    def __getStocksFromFile(self):
        stocks_list_file = open("valid_stocks_list.txt", "r")
        data = stocks_list_file.read()

        return (data)


##########################################################################################
#                      STRATEGIES BUTTONS AND SUPPORTING FUNCTIONS                       #
##########################################################################################

    def __createStrategiesButtons(self):
        """This function creates the buttons for the different strategies.
        """
        blue = "#05d7ff"
        light_blue = "#65e7ff"
        light_green = "#65fff2"
        black = "BLACK"
        background_color = blue

        button_width = 20
        button_height = 2

        column_position = 2
        row_position = 3

        list_size = len(self.__strategies_names)

        for i in range(list_size):
            # This is used to mark the first button as a default button
            if (i == 0):
                background_color = light_green
            else:
                background_color = blue
            
            # Set each button properties
            new_button = Button(self.__root,
                            command=lambda button_name = self.__strategies_names[i]: self.__strategiesFunc(button_name),
                            # command=lambda : self.__print_something(),    
                            text=self.__strategies_names[i],
                            font=("Raleway", 16, "bold"),                           
                            background=background_color,
                            foreground=black,
                            activebackground=light_blue,
                            activeforeground=black,
                            highlightthickness=2,
                            highlightbackground=blue,
                            highlightcolor="WHITE",
                            width=button_width,
                            height=button_height,
                            border=0,
                            cursor="hand1")
        
            # Position each button on the main window grid
            new_button.grid(column=column_position, row=row_position)
            column_position += 1

            # Update the self strategies buttons list
            self.__strategies_buttons.append(new_button)


    def __strategiesFunc(self, button_name):
        """This function gets the button name that was clicked and updates all
        the things that relate to this action.
        """
        self.__strategiesChoice(button_name)
        self.__configureStrategiesButtonsColors(button_name)


    def __strategiesChoice(self, button_name):
        """This function updates the choice of the buttons for the strategies
        0 -> The first button (THREE CANDLES)
        1 -> The second button (HORIZONTAL)
        """

        list_size = len(self.__strategies_buttons)

        for i in range(list_size):
            if (button_name == self.__strategies_names[i]):
                self.__strategy_data["strategy_num"] = i
                self.__strategy_data["strategy_name"] = self.__strategies_names[i]

        if (self.__strategy_data["strategy_name"] == "HORIZONTAL"):
            self.__getUserHorizontalData()


    def __configureStrategiesButtonsColors(self, button_name):
        """This function changes the color of all the strategies buttons
        so that only the one that was lastly clicked is different.
        """
        list_size = len(self.__strategies_buttons)

        for i in range(list_size):
            if (button_name == self.__strategies_names[i]):
                self.__strategies_buttons[i].configure(bg="#65fff2")
            else:
                self.__strategies_buttons[i].configure(bg="#05d7ff")


###########################################################
#        HORIZONTAL STRATEGY SUPPORTING FUNCTIONS         #
###########################################################

    def __getUserHorizontalData(self):
        """This function opens a window in which the user enters the values
        he is intrested to work with.
        In case the user will not enter values they will be set to default
        values.
        """
        horizontal_strategy_window = Toplevel()
        horizontal_strategy_window.geometry("400x400+300+300")

        for i in range(3):
            horizontal_strategy_window.columnconfigure(i, weight=1, uniform='a')
        
        for i in range(6):
            horizontal_strategy_window.rowconfigure(i, weight=1, uniform='a')

        self.__number_of_days = StringVar()
        self.__end_date = StringVar()

        number_of_days_lable = Label(horizontal_strategy_window, text="Number of Days: ")
        number_of_days_lable.grid(column=0, row=1)
        number_of_days_entry = Entry(horizontal_strategy_window, textvariable = self.__number_of_days)
        number_of_days_entry.grid(column=1, row=1)

        end_date_lable = Label(horizontal_strategy_window, text="End Date: ")
        end_date_lable.grid(column=0, row=3)
        end_date_entry = Entry(horizontal_strategy_window, textvariable = self.__end_date)
        end_date_entry.grid(column=1, row=3)

        blue = "#05d7ff"
        light_blue = "#65e7ff"
        light_green = "#65fff2"
        black = "BLACK"
        background_color = blue

        ok_button = Button(horizontal_strategy_window,
                        command=lambda root=horizontal_strategy_window:self.__submitHorizontalAction(horizontal_strategy_window),    
                        text="RUN",
                        font=("Raleway", 16, "bold"),                           
                        background=background_color,
                        foreground=black,
                        activebackground=light_blue,
                        activeforeground=black,
                        highlightthickness=2,
                        highlightbackground=blue,
                        highlightcolor="WHITE",
                        width=20,
                        height=2,
                        border=0,
                        cursor="hand1")
        
        ok_button.grid(column=2, row=5)


    def __submitHorizontalAction(self, window):
        """This function gets the info from the window and closes the window.
        """
        # Getting the info from the window
        number_of_days = self.__number_of_days.get()
        end_date = self.__end_date.get()

        # Making sure that the number of days is valid
        if (number_of_days == ""):
            number_of_days = 7
        else:
            number_of_days = int(number_of_days)

        if (number_of_days < 3):
            number_of_days = 3

        if (number_of_days > 10):
            number_of_days = 10

        # Making sure that the end date is valid
        if (end_date == ""):
            end_date = date.today()
        else:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # Storing the values in the self.__strategy_data to be used later
        self.__strategy_data["number_of_days"] = number_of_days
        self.__strategy_data["end_date"] = end_date

        # TO REMOVE
        # print(self.__stock_prices_data["minimum_price"], self.__stock_prices_data["maximum_price"])

        # Closing the current window
        window.destroy()


##########################################################################################
#                     STOCK LISTS BUTTONS AND SUPPORTING FUNCTIONS                       #
##########################################################################################

    def __createStockListsButtons(self):
        """This function creates the buttons for the different stock lists.
        """
        blue = "#05d7ff"
        light_blue = "#65e7ff"
        light_green = "#65fff2"
        black = "BLACK"
        background_color = blue

        button_width = 20
        button_height = 2

        column_position = 0
        row_position = 1

        status = False

        list_size = len(self.__stock_lists_names)

        for i in range(list_size):
            # This is used to mark the first button as a default button
            if (i == 0):
                background_color = light_green
                status = True
            else:
                background_color = blue
                status = False
            
            # Set the button properties
            new_button = Button(self.__root,
                            command=lambda button_name = self.__stock_lists_names[i]: self.__stockListsFunc(button_name),
                            # command=lambda : self.__print_something(),    
                            text=self.__stock_lists_names[i],
                            font=("Raleway", 16, "bold"),                           
                            background=background_color,
                            foreground=black,
                            activebackground=light_blue,
                            activeforeground=black,
                            highlightthickness=2,
                            highlightbackground=blue,
                            highlightcolor="WHITE",
                            width=button_width,
                            height=button_height,
                            border=0,
                            cursor="hand1")
            
            # Position the button on the main window grid
            new_button.grid(column=column_position, row=row_position)
            row_position += 1

            # Update the self stock prices buttons list
            self.__stock_lists_buttons.append(new_button)

            # Updates the self stock lists choices so that only the basic list is default true
            self.__stock_lists_choices.append(status)


    def __stockListsFunc(self, button_name):
        """This function updates all the things regarding the stock lists
        buttons.
        It updates the self stock lists choices according to the button
        that was clicked.
        It changes the color of the button that was clicked.
        """
        list_size = len(self.__stock_lists_buttons)

        for i in range(list_size):
            # If the button that is clicked was not clicked before it will change to clicked
            if (button_name == self.__stock_lists_names[i] and self.__stock_lists_choices[i] == False):
                self.__stock_lists_choices[i] = True
                self.__stock_lists_buttons[i].configure(bg="#65fff2")

            # If the button that is clicked WAS clicked before it will change to UNClicked    
            elif (button_name == self.__stock_lists_names[i] and self.__stock_lists_choices[i] == True):
                self.__stock_lists_choices[i] = False
                self.__stock_lists_buttons[i].configure(bg="#05d7ff")


##########################################################################################
#                     STOCK PRICES BUTTONS AND SUPPORTING FUNCTIONS                      #
##########################################################################################

    def __createStockPricesButtons(self):
        """This function creates the buttons for the stock prices range.
        """
        blue = "#05d7ff"
        light_blue = "#65e7ff"
        light_green = "#65fff2"
        black = "BLACK"
        background_color = blue

        button_width = 15
        button_height = 2

        column_position = 2
        row_position = 1

        list_size = len(self.__stock_prices_names)

        for i in range(list_size):
            # This is used to mark the first button as a default button
            if (i == 0):
                background_color = light_green
            else:
                background_color = blue

            # Set the button properties
            new_button = Button(self.__root,
                            command=lambda button_name = self.__stock_prices_names[i]: self.__stockPricesFunc(button_name),
                            text=self.__stock_prices_names[i],
                            font=("Raleway", 16, "bold"),                           
                            background=background_color,
                            foreground=black,
                            activebackground=light_blue,
                            activeforeground=black,
                            highlightthickness=2,
                            highlightbackground=blue,
                            highlightcolor="WHITE",
                            width=button_width,
                            height=button_height,
                            border=0,
                            cursor="hand1")
            
            # Position the button on the main window grid
            new_button.grid(column=column_position, row=row_position)
            column_position += 1

            # Update the self stock prices buttons list
            self.__stock_prices_buttons.append(new_button)


    def __stockPricesFunc(self, button_name):
        """This function gets the button name that was clicked and updates all
        the things that relate to this action.
        """
        self.__stockPricesChoice(button_name)
        self.__configureStockPricesButtonsColors(button_name)


    def __stockPricesChoice(self, button_name):
        """This function updates the choice of the buttons for the stock prices
        0 -> The first button (ALL PRICES)
        1 -> The second button (FIXED PRICES)
        2 -> The third button (USER PRICES)
        """
        list_size = len(self.__stock_prices_buttons)

        for i in range(list_size):
            if (button_name == self.__stock_prices_names[i]):
                self.__stock_prices_data.update({"name": self.__stock_prices_names[i]})

        if (self.__stock_prices_data["name"] == "USER PRICES"):
            self.__getUserPriceRange()

        elif (self.__stock_prices_data["name"] == "FIXED PRICES"):
            self.__stock_prices_data["minimum_price"] = 0
            self.__stock_prices_data["maximum_price"] = 100

        else: # self.__stock_prices_data["name"] == "ALL PRICES"
            self.__stock_prices_data["minimum_price"] = 0
            self.__stock_prices_data["maximum_price"] = 500000


    def __configureStockPricesButtonsColors(self, button_name):
        """This function changes the color of all the stock prices buttons
        so that only the one that was lastly clicked is different.
        """
        list_size = len(self.__stock_prices_buttons)

        for i in range(list_size):
            if (button_name == self.__stock_prices_names[i]):
                self.__stock_prices_buttons[i].configure(bg="#65fff2")
            else:
                self.__stock_prices_buttons[i].configure(bg="#05d7ff")


    def __getUserPriceRange(self):
        """This function opens a window in which the user enters the range of
        prices he wants to use.
        """
        price_range_window = Toplevel()
        price_range_window.geometry("400x400+300+300")

        for i in range(3):
            price_range_window.columnconfigure(i, weight=1, uniform='a')
        
        for i in range(6):
            price_range_window.rowconfigure(i, weight=1, uniform='a')

        self.__min_price = StringVar()
        self.__max_price = StringVar()

        min_price_lable = Label(price_range_window, text="Minimum Price: ")
        min_price_lable.grid(column=0, row=1)
        min_price_entry = Entry(price_range_window, textvariable = self.__min_price)
        min_price_entry.grid(column=1, row=1)

        max_price_lable = Label(price_range_window, text="Maximum Price: ")
        max_price_lable.grid(column=0, row=3)
        max_price_entry = Entry(price_range_window, textvariable = self.__max_price)
        max_price_entry.grid(column=1, row=3)

        blue = "#05d7ff"
        light_blue = "#65e7ff"
        light_green = "#65fff2"
        black = "BLACK"
        background_color = blue

        ok_button = Button(price_range_window,
                        command=lambda root=price_range_window:self.__submitPricesAction(price_range_window),    
                        text="RUN",
                        font=("Raleway", 16, "bold"),                           
                        background=background_color,
                        foreground=black,
                        activebackground=light_blue,
                        activeforeground=black,
                        highlightthickness=2,
                        highlightbackground=blue,
                        highlightcolor="WHITE",
                        width=20,
                        height=2,
                        border=0,
                        cursor="hand1")
        
        ok_button.grid(column=2, row=5)


    def __submitPricesAction(self, window):
        """This function gets the info from the window and closes the window.
        """
        # Getting the info from the window
        min_price = self.__min_price.get()
        max_price = self.__max_price.get()

        # Making sure that the minimum price is valid - else it will be 0
        if (min_price == ""):
            min_price = 0
        else:
            min_price = float(min_price)

        if (min_price < 0):
            min_price = 0

        # Making sure that the maximum price is valid - else it will be 500000
        if (max_price == ""):
            max_price = 500000
        else:
            max_price = float(max_price)

        if (max_price < min_price):
            max_price = 500000

        # Storing the values in the self.__stock_prices_data to be used later
        self.__stock_prices_data["minimum_price"] = min_price
        self.__stock_prices_data["maximum_price"] = max_price

        # TO REMOVE
        # print(self.__stock_prices_data["minimum_price"], self.__stock_prices_data["maximum_price"])

        # Closing the current window
        window.destroy()

