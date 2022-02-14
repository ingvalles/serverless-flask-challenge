import logging

from config.secrets import get_secret
from werkzeug.exceptions import HTTPException
from flask import Flask, jsonify

from src.extensions import sieve, jwt, cache
from utils.validators import ValidationException, validations_error_handler


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    if settings_override:
        app.config.update(settings_override)
    

    with app.app_context():
        # Blueprints import
        from .blueprints.credit import credit

        app.register_blueprint(credit)
        extensions(app)

    register_error_handlers(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask app
    :return: None
    """

    sieve.init_app(app)
    jwt.init_app(app)
    cache.init_app(app)

    return None


def register_error_handlers(app):
    app.register_error_handler(
        ValidationException,
        validations_error_handler
    )

    @app.errorhandler(Exception)
    def handle_exception(e):
        if isinstance(e, HTTPException):
            return e

        res = {
            'code': 500,
            'message': 'Something went really wrong!'
        }

        if app.config['DEBUG']:
            file = ''
            line = 0
            tb = e.__traceback__
            while tb is not None:
                if 'src' in tb.tb_frame.f_code.co_filename:
                    file = tb.tb_frame.f_code.co_name
                    line = tb.tb_lineno
                tb = tb.tb_next
            res['message'] = e.message if hasattr(e, 'message') else f'{e}'
            if file != '':
                res['message'] = file + ': ' + str(line) + ' - ' + res['message']

        return jsonify(res), 500


intent = create_app(get_secret())
if __name__ == "__main__":
    logging.basicConfig(filename='error.log', level=logging.DEBUG)

    intent.run()
