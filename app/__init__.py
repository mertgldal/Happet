from flask import Flask, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from functools import wraps

db = SQLAlchemy()
login_manager = LoginManager()
ckeditor = CKEditor()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    Bootstrap5(app)

    login_manager.login_view = "main.login"
    login_manager.login_message_category = "info"

    # Register Blueprints
    from .routes import main
    app.register_blueprint(main)

    # Initialize the database
    with app.app_context():
        db.create_all()

    return app

# User Loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    """Fetch the user from the database by their ID."""
    from .models import User
    return User.query.get(int(user_id))

# Decorator to prevent authenticated users from accessing certain routes
def is_user_authenticated(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if current_user.is_authenticated:
            flash(
                f"You are already logged in! You can't access the {func.__name__} page",
                "danger",
            )
            return redirect(url_for("main.index"))  # Redirect to the home page or another route
        return func(*args, **kwargs)

    return wrapped
