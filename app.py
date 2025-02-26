from flask import Flask, render_template
from routes.bot_routes import bot_blueprint

app = Flask(__name__)

# Importă rutele pentru bot
app.register_blueprint(bot_blueprint)

# Pagina principală
@app.route('/')
def home():
    return render_template('index.html')

# Pagina About
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
