from abc import ABC, abstractmethod

class BaseExchange(ABC):
    """
    Abstract Base Class for all exchange pipelines. 
    Every exchange pipeline must implement the methods defined below.
    """

    @abstractmethod
    def fetch_symbols(self):
        pass

    @abstractmethod
    def fetch_ohlcv(self, symbol, timeframe, since=None, limit=None):
        """
        Fetch OHLCV data for the given symbol and timeframe.
        
        :param symbol: The trading pair symbol (e.g., 'BTCUSD').
        :param timeframe: The timeframe for the OHLCV data (e.g., '1m', '5m', '1h', '1d').
        :param since: Optional. The timestamp in milliseconds to fetch OHLCV data since.
        :param limit: Optional. The maximum number of OHLCV data points to fetch.
        :return: A list of OHLCV data points.
        """
        pass

    @abstractmethod
    def get_order_book(self, symbol):
        pass

    @abstractmethod
    def place_order(self, symbol: str, order_type: int, quantity: float, price=None):
        pass