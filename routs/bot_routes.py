from flask import Blueprint, jsonify
from bot.bot import run_bot

bot_routes = Blueprint('bot_routes', __name__)

@bot_routes.route("/start-bot", methods=["GET"])
def start_bot():
    """
    Pornire bot prin API Flask.
    """
    run_bot()
    return jsonify({"message": "Bot started successfully!"})
