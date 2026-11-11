from flask import render_template


def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(error):
        return render_template(
            "error.html", code=400, message="Requisição inválida."
        ), 400

    @app.errorhandler(404)
    def not_found(error):
        return render_template(
            "error.html", code=404, message="Página não encontrada."
        ), 404

    @app.errorhandler(409)
    def conflict(error):
        return render_template(
            "error.html", code=409, message="Não foi possível concluir: conflito de dados."
        ), 409

    @app.errorhandler(500)
    def internal_error(error):
        return render_template(
            "error.html",
            code=500,
            message="Não foi possível concluir a operação.",
        ), 500