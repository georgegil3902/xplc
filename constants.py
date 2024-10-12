# This file contains all the constants used in the XPLC project.

# Base URLs for different exchanges
BASE_URLS = {
    "Binance": "https://api.binance.com",
    "Bittrex": "https://api.bittrex.com",
    "CoinBasePro": "https://api.pro.coinbase.com",
    "KuCoin": "https://api.kucoin.com"
}

# API endpoints for different exchanges
API_ENDPOINTS = {
    "Binance": "/api/v3",
    "Bittrex": "/api/v1.1",
    "CoinBasePro": "/api/v2",
    "KuCoin": "/api/v1"
}

# API endpoints for account information for different exchanges
ACCOUNT_ENDPOINTS = {
    "Binance": "/api/v3/account",
    "Bittrex": "/api/v1.1/account",
    "CoinBasePro": "/api/v2/accounts",
    "KuCoin": "/api/v1/accounts"
}

# API endpoints for order information for different exchanges
ORDER_ENDPOINTS = {
    "Binance": "/api/v3/order",
    "Bittrex": "/api/v1.1/market/buylimit",
    "CoinBasePro": "/api/v2/orders",
    "KuCoin": "/api/v1/orders"
}

# API endpoints for canceling orders for different exchanges
CANCEL_ORDER_ENDPOINTS = {
    "Binance": "/api/v3/order",
    "Bittrex": "/api/v1.1/market/cancel",
    "CoinBasePro": "/api/v2/orders",
    "KuCoin": "/api/v1/orders"
}

# API endpoints for getting order information for different exchanges
GET_ORDER_ENDPOINTS = {
    "Binance": "/api/v3/order",
    "Bittrex": "/api/v1.1/account/getorder",
    "CoinBasePro": "/api/v2/orders",
    "KuCoin": "/api/v1/orders"
}

# API endpoints for getting all open orders for different exchanges
GET_ALL_OPEN_ORDERS_ENDPOINTS = {
    "Binance": "/api/v3/openOrders",
    "Bittrex": "/api/v1.1/market/getopenorders",
    "CoinBasePro": "/api/v2/orders/open",
    "KuCoin": "/api/v1/orders"
}

# API endpoints for getting all orders for different exchanges
GET_ALL_ORDERS_ENDPOINTS = {
    "Binance": "/api/v3/allOrders",
    "Bittrex": "/api/v1.1/account/getorderhistory",
    "CoinBasePro": "/api/v2/orders",
    "KuCoin": "/api/v1/orders"
}

# API endpoints for getting all trades for different exchanges
GET_ALL_TRADES_ENDPOINTS = {
    "Binance": "/api/v3/myTrades",
    "Bittrex": "/api/v1.1/account/getorderhistory",
    "CoinBasePro": "/api/v2/fills",
    "KuCoin": "/api/v1/fills"
}

# API endpoints for getting all tickers for different exchanges
GET_ALL_TICKERS_ENDPOINTS = {
    "Binance": "/api/v3/ticker/price",
    "Bittrex": "/api/v1.1/public/getticker",
    "CoinBasePro": "/api/v2/prices",
    "KuCoin": "/api/v1/market/orderbook/level1"
}


