import logging
from bot.strategies import basic_strategy
from bot.config import API_KEY

# Configurare loguri
logging.basicConfig(
    filename="logs/bot.log",  # Salvează logurile în logs/bot.log
    level=logging.INFO,  # Setează nivelul de logare
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formatează mesajele de logare
)

def run_bot():
    logging.info("🚀 Botul a fost pornit cu succes!")
    try:
        result = basic_strategy(API_KEY)  # Apelează strategia botului
        logging.info(f"✅ Strategia s-a executat cu succes: {result}")
    except Exception as e:
        logging.error(f"❌ Eroare în rularea botului: {e}")

if __name__ == "__main__":
    run_bot()
