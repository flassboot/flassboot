from flask import Flask
from routes.bot_routes import bot_blueprint  # Import ruta botului
from config.settings import Config  # Import configurarea

app = Flask(__name__)
app.config.from_object(Config)  # Încarcă setările din config

# Înregistrăm blueprint-ul pentru rutele botului
app.register_blueprint(bot_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
