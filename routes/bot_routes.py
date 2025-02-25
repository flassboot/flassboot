from flask import Blueprint, jsonify
from bot.bot import run_bot  # Asigură-te că există bot/bot.py cu funcția run_bot

bot_blueprint = Blueprint("bot_routes", __name__)

@bot_blueprint.route("/start-bot", methods=["GET"])
def start_bot():
    """
    Pornire bot prin API Flask.
    """
    run_bot()
    return jsonify({"message": "Bot started successfully!"})
