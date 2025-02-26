from flask import Flask, render_template
from routes.bot_routes import bot_blue
from routes.web import web

app = Flask(__name__)

# Înregistrează blueprint-urile pentru bot și rutele web
app.register_blueprint(bot_blue)
app.register_blueprint(web)

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
