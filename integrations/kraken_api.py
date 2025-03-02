
import os
from krakenex import API
from dotenv import load_dotenv

# Încarcă variabilele de mediu
load_dotenv()

KRAKEN_API_KEY = os.getenv("KRAKEN_API_KEY")
KRAKEN_API_SECRET = os.getenv("KRAKEN_API_SECRET")

# Conectare la API-ul Kraken
api = API(key=KRAKEN_API_KEY, secret=KRAKEN_API_SECRET)

# Funcție pentru a obține balanța contului
def get_balance():
    try:
        balance = api.query_private('Balance')
        if balance['error']:
            print(f"Error: {balance['error']}")
            return None
        return balance['result']
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

# Funcție pentru a plasa o comandă de cumpărare
def place_buy_order(pair, volume, price):
    try:
        order = api.query_private('AddOrder', {
            'pair': pair,
            'type': 'buy',
            'ordertype': 'limit',
            'price': str(price),
            'volume': str(volume)
        })
        if order['error']:
            print(f"Error: {order['error']}")
            return None
        print(f"Buy order placed: {order['result']}")
        return order['result']
    except Exception as e:
        print(f"Error placing buy order: {e}")
        return None

# Funcție pentru a plasa o comandă de vânzare
def place_sell_order(pair, volume, price):
    try:
        order = api.query_private('AddOrder', {
            'pair': pair,
            'type': 'sell',
            'ordertype': 'limit',
            'price': str(price),
            'volume': str(volume)
        })
        if order['error']:
            print(f"Error: {order['error']}")
            return None
        print(f"Sell order placed: {order['result']}")
        return order['result']
    except Exception as e:
        print(f"Error placing sell order: {e}")
        return None

# Funcție pentru a obține istoricul tranzacțiilor
def get_trade_history():
    try:
        trades = api.query_private('TradesHistory')
        if trades['error']:
            print(f"Error: {trades['error']}")
            return None
        print(f"Trade history: {trades['result']}")
        return trades['result']
    except Exception as e:
        print(f"Error fetching trade history: {e}")
        return None
