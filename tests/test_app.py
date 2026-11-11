import os

from flask import Flask

from app import create_app


def test_create_app_returns_flask_instance():
    application = create_app({"TESTING": True, "DATABASE": ":memory:"})
    assert isinstance(application, Flask)


def test_default_config_is_not_testing():
    application = create_app({"DATABASE": ":memory:"})
    assert application.config["TESTING"] is False


def test_test_config_overrides_defaults():
    application = create_app(
        {"TESTING": True, "SECRET_KEY": "abc", "DATABASE": ":memory:"}
    )
    assert application.config["TESTING"] is True
    assert application.config["SECRET_KEY"] == "abc"
    assert application.config["DATABASE"] == ":memory:"


def test_database_defaults_to_instance_path():
    application = create_app({"DATABASE": None})
    assert application.config["DATABASE"] == os.path.join(
        application.instance_path, "mathlab.sqlite"
    )


def test_instance_directory_exists(app):
    assert os.path.isdir(app.instance_path)


def test_difficulty_and_alternative_limits(app):
    assert app.config["DIFFICULTIES"] == ("Fácil", "Médio", "Difícil")
    assert app.config["MIN_ALTERNATIVES"] == 2
    assert app.config["MAX_ALTERNATIVES"] == 6


def test_client_fixture_is_usable(client):
    assert client is not None