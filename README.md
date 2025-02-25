import os
import datetime
import json
import time
import logging
import requests
import threading
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output, State
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import tweepy
from newsapi import NewsApiClient
import discord
from discord.ext import commands
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
import sqlite3

Cargar claves API desde un archivo .env

load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
NEWS_API_KEY = os.getenv("GOOGLE_NEWS_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_PORT = os.getenv("MAIL_PORT")
MAIL_USE_TLS = True
MAIL_USE_SSL = False

Configurar Flask

app = Flask(name)
bcrypt = Bcrypt(app)
app.secret_key = SECRET_KEY

Configurar Mail

app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = int(MAIL_PORT)
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
mail = Mail(app)

Configurar SQLite pentru stocare useri

def init_db():
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, email TEXT, password TEXT, trial_end DATE, subscription_active INTEGER DEFAULT 0)''')
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
    cursor.execute("INSERT INTO users (username, email, password, trial_end, subscription_active) VALUES (?, ?, ?, ?, 0)", (username, email, password, trial_end))  
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

if name == "main":
app.run(host='0.0.0.0', port=5000, debug=True)
...
