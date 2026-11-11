import hmac
import secrets

from flask import abort, request, session

SESSION_KEY = "_csrf_token"
FORM_FIELD = "_csrf_token"
HEADER = "X-CSRFToken"
SAFE_METHODS = ("GET", "HEAD", "OPTIONS", "TRACE")


def generate_csrf_token():
    token = session.get(SESSION_KEY)
    if not token:
        token = secrets.token_urlsafe(32)
        session[SESSION_KEY] = token
    return token


def _submitted_token():
    return request.form.get(FORM_FIELD) or request.headers.get(HEADER)


def validate_csrf_token():
    expected = session.get(SESSION_KEY)
    received = _submitted_token()
    if not expected or not received or not hmac.compare_digest(expected, received):
        abort(400, description="CSRF token ausente ou inválido.")


def init_app(app):
    @app.before_request
    def protect_from_csrf():
        if request.method not in SAFE_METHODS:
            validate_csrf_token()

    @app.context_processor
    def inject_csrf_token():
        return {"csrf_token": generate_csrf_token}