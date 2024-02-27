

class Candle:
    """A class that creates a stock 'Candle'
    It will have the major sections that build a 'Candle'
    in a candles chart of the stock market.
    """
    __stock_symbol = 0
    __serial_number = 0
    __date = 0
    __open_price = 0
    __close_price = 0
    __high_price = 0
    __low_price = 0
    __volume = 0

    def __init__(self, stock_symbol, serial_number, date, open, close, high, low, volume):
        self.__stock_symbol = stock_symbol
        self.__serial_number = serial_number
        self.__date = date
        self.__open_price = open
        self.__close_price = close
        self.__high_price = high
        self.__low_price = low
        self.__volume = volume

    def getStockSymbol(self):
        return (self.__stock_symbol)
    
    def getSerialNumber(self):
        return (self.__serial_number)
    
    def getDate(self):
        return (self.__date)
    
    def getOpen(self):
        return (self.__open_price)
    
    def getClose(self):
        return (self.__close_price)
    
    def getHigh(self):
        return (self.__high_price)
    
    def getLow(self):
        return (self.__low_price)
    
    def getVolume(self):
        return (self.__volume)
    
    def printCandle(self):
        print(f"Stock Symbol: {self.__stock_symbol}")
        print(f"Serial Number: {self.__serial_number}")
        print(f"Date: {self.__date}")
        print(f"Open: {self.__open_price}")
        print(f"Close: {self.__close_price}")
        print(f"High: {self.__high_price}")
        print(f"Low: {self.__low_price}")
        print(f"Volume: {self.__volume}")