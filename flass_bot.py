import os
import time
import json
import requests
import logging
import threading
import sqlite3
import datetime
from dotenv import load_dotenv
from binance.client import Client
from binance.enums import *
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from fastapi import FastAPI
import uvicorn

# 📌 1️⃣ Încarcă variabilele de mediu
load_dotenv()
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

# 📌 2️⃣ Conectare la Binance API
client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

# 📌 3️⃣ Clasa pentru Trading Bot
class FlassBot:
    def __init__(self):
        self.running = False
        print("🚀 Flass Trading Bot Initialized!")

    def check_market_conditions(self):
        print("📊 Checking market conditions...")
        # Simulare analiză de piață
        time.sleep(5)

    def start(self):
        if self.running:
            print("✅ Bot is already running!")
            return
        self.running = True
        print("🚀 Bot started!")
        while self.running:
            self.check_market_conditions()

    def stop(self):
        self.running = False
        print("🛑 Bot stopped.")

bot = FlassBot()

# 📌 4️⃣ Creare API FastAPI pentru control bot
api = FastAPI()

@api.get("/")
def home():
    return {"message": "Flass Trading Bot API is running!"}

@api.get("/start")
def start_bot():
    if not bot.running:
        threading.Thread(target=bot.start).start()
        return {"status": "Bot started"}
    return {"status": "Bot already running"}

@api.get("/stop")
def stop_bot():
    if bot.running:
        bot.stop()
        return {"status": "Bot stopped"}
    return {"status": "Bot is not running"}

@api.get("/status")
def get_status():
    return {"running": bot.running}

# 📌 5️⃣ Configurare Flask pentru interfață web
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "supersecretkey"

# 📌 6️⃣ Configurare bază de date SQLite
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, username TEXT, email TEXT, password TEXT, trial_end DATE, subscription_active INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        trial_end = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime('%Y-%m-%d')

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password, trial_end, subscription_active) VALUES (?, ?, ?, ?, 0)",
                       (username, email, password, trial_end))
        conn.commit()
        conn.close()

        flash("Registration successful! You have a 7-day free trial.", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user[3], password):
            trial_end = datetime.datetime.strptime(user[4], '%Y-%m-%d')
            if datetime.datetime.now() > trial_end and user[5] == 0:
                flash("Your free trial has expired. Please subscribe to continue.", "danger")
                return redirect(url_for('subscribe'))
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials! Try again.", "danger")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        username = request.form['username']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET subscription_active = 1 WHERE username = ?", (username,))
        conn.commit()
        conn.close()
        flash("Subscription activated manually!", "success")
        return redirect(url_for('login'))
    return render_template('subscribe.html')

# 📌 7️⃣ Pornirea simultană a FastAPI și Flask
if __name__ == "__main__":
    threading.Thread(target=lambda: uvicorn.run(api, host="0.0.0.0", port=8000)).start()
    app.run(host="0.0.0.0", port=5000, debug=True)
