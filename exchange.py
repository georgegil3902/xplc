from abc import ABC, abstractmethod

import requests

import constants as const

class Exchange(ABC):
    """
    Abstract Base Class for all exchange pipelines. 
    Every exchange pipeline must implement the methods defined below.
    """

    def __init__(self, api_key: str = None, api_secret: str = None) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.exchange_name = self.__class__.__name__
        self.base_url = const.BASE_URLS[self.exchange_name]

    @abstractmethod
    def fetch_symbols(self):
        pass
    
    def fetch_tickers(self):
        pass
        
    def fetch_order_book(self, symbol):
        pass

    def fetch_trades(self, symbol):
        pass

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

    def fetch_24hr_stats(self, symbol):
        pass
    
    def get_trade_fees(self, symbol: str, order_type: int, quantity: float, price=None):
        """
        Get the trade fees for the given symbol, order type, quantity, and price.
        
        :param symbol: The trading pair symbol (e.g., 'BTCUSD').
        :param order_type: The type of order (e.g., 1 for market order, 2 for limit order).
        :param quantity: The quantity of the order.
        :param price: Optional. The price of the order.
        :return: A dictionary containing the maker and taker fees.
        """
        pass   
    
    def place_order(self, symbol: str, order_type: int, quantity: float, price=None):
        pass
    
    def fetch_order_status(self, order_id):
        pass

    def cancel_order(self, order_id):
        pass

    def fetch_account_info(self):    
        pass

    def fetch_open_orders(self):
        pass

    def fetch_account_snapshot(self):
        pass

    def withdraw_funds(self, asset, amount, address):
        pass

    def fetch_deposit_address(self, asset):
        pass

    def fetch_withdraw_history(self, asset=None, start_time=None, end_time=None):
        pass