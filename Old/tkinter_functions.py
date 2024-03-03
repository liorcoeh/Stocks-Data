import tkinter as tk
# from button import *


price_button_index = 0


def set_root(root):
    """This function sets the size of the root window of the program.
    """
    window_width = decide_window_width(root)
    window_height = decide_window_height(root)

    x_position = decide_window_horizontal_position(root)
    y_position = decide_window_vertical_position(root)

    columns_amount = get_column_amount()
    rows_amount = get_row_amount()

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    for i in range(columns_amount):
        root.columnconfigure(i, weight=1, uniform='a')

    for i in range(rows_amount):
        root.rowconfigure(i, weight=1, uniform='a')


    # label1 = tk.Label(root, text="lable1", background="red")
    # label1.grid(row = 0, column=0)

    # label2 = tk.Label(root, text="lable2", background="red")
    # label2.grid(row=2, column=2)

    # label3 = tk.Label(root, text="lable3", background="red")
    # label3.grid(row=rows_amount-1, column=columns_amount-1)


def create_buttons(root):
    __create_run_button(root)
    __create_strategies_buttons(root)
    __create_stock_lists_buttons(root)
    __create_stock_prices_buttons(root)

# TO REMOVE AFTER ALL THE RIGHT FUNCTIONS WERE CREATED
def print_some():
     print("NEEDS TO CREATE A FUNCTION")

def print_something_else():
    print("PRINTING")

###########################################################################
#            SETTING THE WINDOW SIZE AND POSISTION FUNCTIONS              #
###########################################################################

# GETTING THE PHYSICAL SCREEN'S SIZE
def get_screen_width(root):
    """A function that returns the widthe of the screen on which the program
    is running on, in pixles.
    """
    screen_width = root.winfo_screenwidth()

    return (screen_width)

def get_screen_height(root):
    """A function that returns the height of the screen on which the program
    is running on, in pixels.
    """
    screen_height = root.winfo_screenheight()

    return (screen_height)

# CALCULATING THE PROGRAM WINDOW'S SIZE
def decide_window_width(root):
    """This function will fit the window to a standrad pc screen width of
    a 1920 pixels (or less, if the screen is smaller).
    """
    default_screen_width = 1920
    this_screen_width = get_screen_width(root)

    if (this_screen_width > default_screen_width):
        return (default_screen_width)
    else:
        return (this_screen_width)

def decide_window_height(root):
    """This function will fit the window to a standrad pc screen height of
    a 1080 pixels (or less, if the screen is smaller).
    """
    default_screen_height = 1080
    this_screen_height = get_screen_height(root)

    if (this_screen_height > default_screen_height):
        return (default_screen_height)
    else:
        return (this_screen_height)

# CALCULATING THE POSTION OF THE PROGRAM'S WINDOW
def decide_window_horizontal_position(root):
    """This function will decided the horizontal position to put the
    window so it will appear at the middle of the screen.
    """
    this_screen_width = get_screen_width(root)

    window_width = decide_window_width(root)

    if (window_width < this_screen_width):
        x_position = (this_screen_width / 2) - (window_width / 2)
    else:
        x_position = 0

    # It must return an int cause that is what the functions use
    return (int(x_position))

def decide_window_vertical_position(root):
    """This function will decided the vertical position to put the
    window so it will appear at the middle of the screen.
    """
    this_screen_height = get_screen_height(root)

    window_height = decide_window_height(root)

    if (window_height < this_screen_height):
        y_position = (this_screen_height / 2) - (window_height / 2)
    else:
        y_position = 0

    # It must return an int cause that is what the functions use
    return (int(y_position))

# CALCULATING THE NUMBER OF COLUMNS AND ROWS OF THE PROGRAM'S WINDOW
def get_column_amount():
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

def get_row_amount():
    """This function sets how many rows the window of the program will have,
    it is based on the number to stocks list that exists in the program.
    """
    min_row_num = 10
    stocks_list_num = 3

    if (stocks_list_num >= min_row_num):
        return (stocks_list_num)
    else:
        return (min_row_num)


###########################################################################
#                    CREATING THE BUTTONS FUNCTIONS                       #
###########################################################################

def __create_run_button(root):
    """This function creates the button for the run function.
    """
    button_font = "Raleway"
    button_bg_color = "#20bebe"
    button_fg_color = "white"
    button_height = 2
    button_width = 20

    column_position = get_column_amount() - 1
    row_position = get_row_amount() - 1

    run_button_text = tk.StringVar()
    run_button_text.set("RUN")

    run_button = tk.Button(root, textvariable=run_button_text, command=lambda: [__print_price_button_index(), __change_button_color(run_button)],
                    font=button_font, bg=button_bg_color, fg=button_fg_color, height=button_height, width=button_width)
    run_button.grid(column=column_position, row=row_position)


def __create_strategies_buttons(root):
    """This function creates the buttons for the different strategies.
    """
    button_font = "Raleway"
    button_bg_color = "#20bebe"
    button_fg_color = "white"
    button_height = 2
    button_width = 20

    three_candles_button_text = tk.StringVar()
    three_candles_button_text.set("THREE CANDLES")

    three_candles_button = tk.Button(root, textvariable=three_candles_button_text, command=lambda:print_some(),
                                font=button_font, bg=button_bg_color, fg=button_fg_color, height=button_height, width=button_width)
    three_candles_button.grid(column=2, row=2)

    horizontal_button_text = tk.StringVar()
    horizontal_button_text.set("HORIZONTAL")

    horizontal_button = tk.Button(root, textvariable=horizontal_button_text, command=lambda:print_some(),
                            font=button_font, bg=button_bg_color, fg=button_fg_color, height=button_height, width=button_width)
    horizontal_button.grid(column=3, row=2)


def __create_stock_lists_buttons(root):
    """This function creates the buttons for the different stock lists.
    """
    button_font = "Raleway"
    button_bg_color = "#20bebe"
    button_fg_color = "white"
    button_height = 2
    button_width = 20

    # Basic stocks
    basic_stocks_button_text = tk.StringVar()
    basic_stocks_button_text.set("BASIC STOCKS")

    basic_stocks_button = tk.Button(root, textvariable=basic_stocks_button_text, command=lambda:print_some(),
                            font=button_font, bg=button_bg_color, fg=button_fg_color, height=button_height, width=button_width)
    basic_stocks_button.grid(column=0, row=0)

    # S&P 500 stocks
    sp_stocks_button_text = tk.StringVar()
    sp_stocks_button_text.set("S&P 500 STOCKS")

    sp_stocks_button = tk.Button(root, textvariable=sp_stocks_button_text, command=lambda:print_some(),
                        font=button_font, bg=button_bg_color, fg=button_fg_color, height=button_height, width=button_width)
    sp_stocks_button.grid(column=0, row=1)

    # Nasdaq 100 stocks
    nasdaq_stocks_button_text = tk.StringVar()
    nasdaq_stocks_button_text.set("NASDAQ 100 STOCKS")

    nasdaq_stocks_button = tk.Button(root, textvariable=nasdaq_stocks_button_text, command=lambda:print_some(),
                            font=button_font, bg=button_bg_color, fg=button_fg_color, height=button_height, width=button_width)
    nasdaq_stocks_button.grid(column=0, row=2)

    # Leveraged stocks
    leveraged_stocks_button_text = tk.StringVar()
    leveraged_stocks_button_text.set("LEVERAGED STOCKS")

    leveraged_stocks_button = tk.Button(root, textvariable=leveraged_stocks_button_text, command=lambda:print_some(),
                                font=button_font, bg=button_bg_color, fg=button_fg_color, height=button_height, width=button_width)
    leveraged_stocks_button.grid(column=0, row=3)


def __create_stock_prices_buttons(root):
    """This function creates the buttons for the stock prices range.
    """
    button_font = "Raleway"
    button_bg_color = "#2F3C7E"
    button_fg_color = "white"
    button_height = 2
    button_width = 20

    # The stocks have no selection based on a price range - default?
    all_prices_button_text = tk.StringVar()
    all_prices_button_text.set("ALL PRICES")

    all_prices_button = tk.Button(root, textvariable=all_prices_button_text,
                        command=lambda: [__update_price_button_index(1), __click_price_button()],
                        font=button_font, bg=button_bg_color, fg=button_fg_color, height=button_height, width=button_width)
    all_prices_button.grid(column=2, row=0)


    # The stocks have a selection based on a 0 minimum and 100 maximum price range
    fixed_prices_button_text = tk.StringVar()
    fixed_prices_button_text.set("FIXED PRICES")

    fixed_prices_button = tk.Button(root, textvariable=fixed_prices_button_text, command=lambda: __update_price_button_index(2),
                        font=button_font, bg=button_bg_color, fg=button_fg_color, height=button_height, width=button_width)
    fixed_prices_button.grid(column=3, row=0)

    # The stocks will have selection based on prices given by the user
    user_prices_button_text = tk.StringVar()
    user_prices_button_text.set("USER PRICES")

    user_prices_button = tk.Button(root, textvariable=user_prices_button_text, command=lambda: __update_price_button_index(3),
                        font=button_font, bg=button_bg_color, fg=button_fg_color, height=button_height, width=button_width)
    user_prices_button.grid(column=4, row=0)


def __change_button_color(button):
    button.configure(bg="yellow")

def __click_price_button(self):
    self.fixed_prices_button.configure(bg="yellow")

def __update_price_button_index(index):
    global price_button_index
    price_button_index = index

def __print_price_button_index():
    print(price_button_index)

# # TO USE LATER
# def changeOnHover(button, color_on_hover, color_on_leave):
#     """A function that changes the button's color when you hover over
#     it with the mouse.
#     """

#     # When 'entring' the widget of the button, will change the background color
#     button.bind("<Enter", func=lambda e: button.config(background=color_on_hover))

#     button.bind("<Leave", func=lambda e: button.config(background=color_on_leave))