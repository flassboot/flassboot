from flask import Blueprint

bot_blue = Blueprint('bot', __name__)

@bot_blue.route('/bot')
def bot_home():
    return "FlaskBot API is running!"
