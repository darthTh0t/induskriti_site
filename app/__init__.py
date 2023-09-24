from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    """Create and configure an instance of the Flask application."""
    
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    mail.init_app(app)

    with app.app_context():
        from . import views
        return app