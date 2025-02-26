from flask import Blueprint

bot_blueprint = Blueprint('bot', __name__)

@bot_blueprint.route('/bot')
def bot_home():
    return "FlaskBot API is running!"
