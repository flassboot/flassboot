
import os
from kucoin.client import Client
from dotenv import load_dotenv

# Încarcă variabilele de mediu
load_dotenv()

KUCOIN_API_KEY = os.getenv("KUCOIN_API_KEY")
KUCOIN_API_SECRET = os.getenv("KUCOIN_API_SECRET")
KUCOIN_API_PASSPHRASE = os.getenv("KUCOIN_API_PASSPHRASE")

# Conectare la API-ul KuCoin
client = Client(KUCOIN_API_KEY, KUCOIN_API_SECRET, KUCOIN_API_PASSPHRASE)

# Funcție pentru a obține balanța contului
def get_balance():
    try:
        accounts = client.get_accounts()
        for account in accounts:
            if account['currency'] == 'USDT':
                return f"USDT Balance: {account['balance']}"
        return "USDT Balance not found."
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

# Funcție pentru a plasa o comandă de cumpărare
def place_buy_order(symbol, amount, price):
    try:
        order = client.create_limit_order(symbol, 'buy', amount, price)
        print(f"Buy order placed: {order}")
        return order
    except Exception as e:
        print(f"Error placing buy order: {e}")
        return None

# Funcție pentru a plasa o comandă de vânzare
def place_sell_order(symbol, amount, price):
    try:
        order = client.create_limit_order(symbol, 'sell', amount, price)
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
