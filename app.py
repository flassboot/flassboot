from flask import Flask
from routes.bot_routes import bot_routes

app = Flask(__name__)

# Adăugare blueprint pentru bot
app.register_blueprint(bot_routes, url_prefix="/bot")

if __name__ == "__main__":
    app.run(debug=True)
