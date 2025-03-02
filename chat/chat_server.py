
import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from dotenv import load_dotenv

# Încarcă variabilele de mediu
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "supersecretkey")
socketio = SocketIO(app)

# Gestionare eveniment de conectare
@socketio.on('connect')
def handle_connect():
    print("🔗 A user connected.")
    emit('message', {'msg': 'Welcome to the FlassTradingBoot Chat!'})

# Gestionare eveniment de deconectare
@socketio.on('disconnect')
def handle_disconnect():
    print("❌ A user disconnected.")

# Gestionare mesaje
@socketio.on('send_message')
def handle_send_message(data):
    print(f"📩 Received message: {data['msg']}")
    emit('message', {'msg': data['msg'], 'user': data['user']}, broadcast=True)

# Pagină principală a chat-ului
@app.route('/chat')
def chat():
    return render_template('chat.html')

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5001, debug=True)
