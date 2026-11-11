def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"MathLab" in response.data


def test_unknown_route_returns_404(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404


def test_foreign_keys_enabled(app):
    with app.app_context():
        from app.db import get_db

        value = get_db().execute("PRAGMA foreign_keys").fetchone()[0]
        assert value == 1


def test_db_connection_reused_within_context(app):
    with app.app_context():
        from app.db import get_db

        assert get_db() is get_db()


def test_autoescape_enabled_for_html(app):
    assert app.jinja_env.autoescape("question.html") is True
    assert app.jinja_env.autoescape("plain.txt") is False


def test_post_without_csrf_is_rejected(app, client):
    app.add_url_rule("/_probe", "_probe", lambda: "ok", methods=["POST"])
    response = client.post("/_probe")
    assert response.status_code == 400


def test_post_with_valid_csrf_passes(app, client):
    app.add_url_rule("/_probe2", "_probe2", lambda: "ok", methods=["POST"])
    with client.session_transaction() as session:
        session["_csrf_token"] = "known-token"
    response = client.post("/_probe2", data={"_csrf_token": "known-token"})
    assert response.status_code == 200
    assert response.data == b"ok"


def test_409_handler_renders_error_page(app, client):
    from flask import abort

    app.add_url_rule("/_conflict", "_conflict", lambda: abort(409))
    response = client.get("/_conflict")
    assert response.status_code == 409
    assert b"409" in response.data