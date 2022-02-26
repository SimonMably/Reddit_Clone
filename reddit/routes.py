import os
from datetime import datetime as dt
from functools import wraps

from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from reddit import app, db, login_manager
from reddit.models import User, Post, Comment
from reddit.forms import RegisterUserForm, CreatePost, CreateComment


@app.context_processor
def inject_now():
    """Allows the placing of the current date in to associated web pages."""
    return {"now": dt.now()}


def admin_only(f):
    """Decorator: Gives user with id of 1 admin status to perform certain
    actions / access certain features."""
    @wraps(f)
    def admin_func(*args, **kwargs):
        # TODO: May need to allow other users to have admin status
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return admin_func


def mod_only(f):
    """Decorator: Gives users moderator status, particularly users who control
    sub-reddits. Users with moderator status have particular privelages, eg. 
    deleting posts and comments."""
    # TODO: Complete
    @wraps(f)
    def mod_func(*args, **kwargs):
        # TODO: Find a way to give users moderator status
        pass
    return mod_func      


@login_manager.user_loader
def load_user(user_id: int):
    """Uses user_loader decorator from LoginManager(). Loads user, when signing 
    in via the retrieval of users ID from Admin table of database."""
    return User.query.get(int(user_id))


@app.route("/")
@app.route("/home")
def homepage():
    """"""
    pass


@app.route("/register-user", method=["GET", "POST"])
def register_user():
    """"""
    pass


@app.route("/login-user", method=["GET", "POST"])
def login_user():
    """"""
    pass


@app.route("/logout-user")
def logout_user():
    """"""
    pass


# TODO: Add routes for creating sub-reddits
# TODO: Add routes for deleting sub-reddets
# TODO: Add routes for creating posts
# TODO: Add routes for deleting posts
# TODO: Add routes for creating comments
# TODO: Add routes for deleting comments
# TODO: Add routes for deleting users














