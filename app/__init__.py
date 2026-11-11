import os

from flask import Flask

from . import db, errors, security
from .blueprints import attempts, history, main, questions
from .config import Config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    if test_config is not None:
        app.config.from_mapping(test_config)

    if not app.config.get("DATABASE"):
        app.config["DATABASE"] = os.path.join(app.instance_path, "mathlab.sqlite")

    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)
    errors.register_error_handlers(app)
    security.init_app(app)

    app.register_blueprint(main.bp)
    app.register_blueprint(questions.bp)
    app.register_blueprint(attempts.bp)
    app.register_blueprint(history.bp)

    return app