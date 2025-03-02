
import os
from bitfinex.client import ClientV2
from dotenv import load_dotenv

# Încarcă variabilele de mediu
load_dotenv()

BITFINEX_API_KEY = os.getenv("BITFINEX_API_KEY")
BITFINEX_API_SECRET = os.getenv("BITFINEX_API_SECRET")

# Conectare la API-ul Bitfinex
client = ClientV2(api_key=BITFINEX_API_KEY, api_secret=BITFINEX_API_SECRET)

# Funcție pentru a obține balanța contului
def get_balance():
    try:
        balances = client.balances()
        for balance in balances:
            if balance[1] == 'USDT':
                return f"USDT Balance: {balance[2]}"
        return "USDT Balance not found."
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

# Funcție pentru a plasa o comandă de cumpărare
def place_buy_order(symbol, amount, price):
    try:
        order = client.new_order(
            symbol=symbol,
            amount=str(amount),
            price=str(price),
            side='buy',
            type='exchange limit'
        )
        print(f"Buy order placed: {order}")
        return order
    except Exception as e:
        print(f"Error placing buy order: {e}")
        return None

# Funcție pentru a plasa o comandă de vânzare
def place_sell_order(symbol, amount, price):
    try:
        order = client.new_order(
            symbol=symbol,
            amount=str(amount),
            price=str(price),
            side='sell',
            type='exchange limit'
        )
        print(f"Sell order placed: {order}")
        return order
    except Exception as e:
        print(f"Error placing sell order: {e}")
        return None

# Funcție pentru a obține istoricul tranzacțiilor
def get_trade_history(symbol):
    try:
        trades = client.trades(symbol=symbol)
        print(f"Trade history for {symbol}: {trades}")
        return trades
    except Exception as e:
        print(f"Error fetching trade history: {e}")
        return None
