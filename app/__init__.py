import os

from flask import Flask

from .config import Config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    if test_config is not None:
        app.config.from_mapping(test_config)

    if not app.config.get("DATABASE"):
        app.config["DATABASE"] = os.path.join(app.instance_path, "mathlab.sqlite")

    os.makedirs(app.instance_path, exist_ok=True)

    return app