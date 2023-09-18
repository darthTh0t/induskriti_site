from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """Create and configure an instance of the Flask application."""
    
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import views
        return app