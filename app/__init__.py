import os

from flask import Flask, request, current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from app.auth import bp as bp_auth
    app.register_blueprint(bp_auth)

    from app.report import bp as bp_report
    app.register_blueprint(bp_report)

    from app.collect import bp as bp_survey
    app.register_blueprint(bp_survey)

    db.init_app(app)

    return app

from app import models