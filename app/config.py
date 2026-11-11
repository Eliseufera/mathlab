import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "mathlab-dev-secret-key-change-me")
    DATABASE = os.environ.get("MATHLAB_DATABASE")
    TESTING = False

    DIFFICULTIES = ("Fácil", "Médio", "Difícil")
    MIN_ALTERNATIVES = 2
    MAX_ALTERNATIVES = 6
    MAX_STATEMENT_LENGTH = 2000
    MAX_ALTERNATIVE_LENGTH = 500