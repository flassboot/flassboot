import os

class Config:
    """ Configurație pentru aplicație """
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
