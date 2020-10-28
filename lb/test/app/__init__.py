from flask import Flask
from flask_bs4 import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_bcrypt import BCrypt

app = Flask(__name__)
bot = Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = BCrypt(app)
app.config.from_object(Config)

from app.routes import *
