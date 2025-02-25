import logging
from bot.strategies import basic_strategy
from bot.config import API_KEY, API_SECRET

# Configurare loguri
logging.basicConfig(filename="logs/bot.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def run_bot():
    logging.info("🚀 Botul a fost pornit!")
    try:
        result = basic_strategy()
        logging.info(f"✅ Strategie executată: {result}")
    except Exception as e:
        logging.error(f"❌ Eroare în bot: {e}")

if __name__ == "__main__":
    run_bot()
