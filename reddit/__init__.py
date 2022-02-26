from datetime import datetime as dt
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, login_required, logout_user, current_user, LoginManager
from flask_gravatar import Gravatar

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL", "sqlite:///database.db")
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from reddit import routes
