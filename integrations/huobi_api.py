
import os
from huobi.client.trade import TradeClient
from huobi.client.account import AccountClient
from huobi.client.market import MarketClient
from dotenv import load_dotenv

# Încarcă variabilele de mediu
load_dotenv()

HUOBI_API_KEY = os.getenv("HUOBI_API_KEY")
HUOBI_API_SECRET = os.getenv("HUOBI_API_SECRET")

# Conectare la API-ul Huobi
account_client = AccountClient(api_key=HUOBI_API_KEY, secret_key=HUOBI_API_SECRET)
trade_client = TradeClient(api_key=HUOBI_API_KEY, secret_key=HUOBI_API_SECRET)
market_client = MarketClient()

# Funcție pentru a obține balanța contului
def get_balance():
    try:
        accounts = account_client.get_account_balance()
        for account in accounts:
            if account.currency == 'usdt':
                return f"USDT Balance: {account.balance}"
        return "USDT Balance not found."
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

# Funcție pentru a plasa o comandă de cumpărare
def place_buy_order(symbol, amount, price):
    try:
        order_id = trade_client.create_order(symbol=symbol, account_type='spot', order_type='buy-limit', amount=amount, price=price)
        print(f"Buy order placed: {order_id}")
        return order_id
    except Exception as e:
        print(f"Error placing buy order: {e}")
        return None

# Funcție pentru a plasa o comandă de vânzare
def place_sell_order(symbol, amount, price):
    try:
        order_id = trade_client.create_order(symbol=symbol, account_type='spot', order_type='sell-limit', amount=amount, price=price)
        print(f"Sell order placed: {order_id}")
        return order_id
    except Exception as e:
        print(f"Error placing sell order: {e}")
        return None

# Funcție pentru a obține istoricul tranzacțiilor
def get_trade_history(symbol):
    try:
        trades = market_client.get_recent_trades(symbol=symbol, size=20)
        print(f"Trade history for {symbol}: {trades}")
        return trades
    except Exception as e:
        print(f"Error fetching trade history: {e}")
        return None
