
import os
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv

# Încarcă variabilele de mediu
load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

# Conectare la API-ul Binance
client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

# Funcție pentru a obține balanța contului
def get_balance():
    try:
        balances = client.get_asset_balance(asset='USDT')
        return f"USDT Balance: {balances['free']}"
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

# Funcție pentru a plasa o comandă de cumpărare
def place_buy_order(symbol, quantity, price):
    try:
        order = client.create_order(
            symbol=symbol,
            side=SIDE_BUY,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=str(price)
        )
        print(f"Buy order placed: {order}")
        return order
    except Exception as e:
        print(f"Error placing buy order: {e}")
        return None

# Funcție pentru a plasa o comandă de vânzare
def place_sell_order(symbol, quantity, price):
    try:
        order = client.create_order(
            symbol=symbol,
            side=SIDE_SELL,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=str(price)
        )
        print(f"Sell order placed: {order}")
        return order
    except Exception as e:
        print(f"Error placing sell order: {e}")
        return None

# Funcție pentru a obține istoricul tranzacțiilor
def get_trade_history(symbol):
    try:
        trades = client.get_my_trades(symbol=symbol)
        print(f"Trade history for {symbol}: {trades}")
        return trades
    except Exception as e:
        print(f"Error fetching trade history: {e}")
        return None
