
import os
import cbpro
from dotenv import load_dotenv

# Încarcă variabilele de mediu
load_dotenv()

COINBASE_API_KEY = os.getenv("COINBASE_API_KEY")
COINBASE_API_SECRET = os.getenv("COINBASE_API_SECRET")
COINBASE_API_PASSPHRASE = os.getenv("COINBASE_API_PASSPHRASE")

# Conectare la API-ul Coinbase Pro
client = cbpro.AuthenticatedClient(COINBASE_API_KEY, COINBASE_API_SECRET, COINBASE_API_PASSPHRASE)

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
def place_buy_order(product_id, amount, price):
    try:
        order = client.place_limit_order(
            product_id=product_id,
            side='buy',
            price=str(price),
            size=str(amount)
        )
        print(f"Buy order placed: {order}")
        return order
    except Exception as e:
        print(f"Error placing buy order: {e}")
        return None

# Funcție pentru a plasa o comandă de vânzare
def place_sell_order(product_id, amount, price):
    try:
        order = client.place_limit_order(
            product_id=product_id,
            side='sell',
            price=str(price),
            size=str(amount)
        )
        print(f"Sell order placed: {order}")
        return order
    except Exception as e:
        print(f"Error placing sell order: {e}")
        return None

# Funcție pentru a obține istoricul tranzacțiilor
def get_trade_history(product_id):
    try:
        fills = client.get_fills(product_id=product_id)
        trades = list(fills)
        print(f"Trade history for {product_id}: {trades}")
        return trades
    except Exception as e:
        print(f"Error fetching trade history: {e}")
        return None
