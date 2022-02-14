from flask import current_app, jsonify
from flask_sieve import FormRequest, ValidationException  # noqa
from datetime import datetime, date

def validations_error_handler(ex):
    response = {
        'code': current_app.config.get('SIEVE_ERROR_CODE', 'TEMP0001'),
        'message': current_app.config.get('SIEVE_RESPONSE_MESSAGE', 'Validation error'),
        'errors': ex.errors
    }

    if current_app.config.get('SIEVE_INCLUDE_SUCCESS_KEY'):
        response['success'] = False

    if current_app.config.get('SIEVE_RESPONSE_WRAPPER'):
        response = {current_app.config.get('SIEVE_RESPONSE_WRAPPER'): response}

    return jsonify(response), current_app.config.get('SIEVE_INVALID_STATUS_CODE', 400)


def get_class(kls):
    """
    Dynamically get an object of the specified class

    :param kls: str
    :return: obj
    """

    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


def validate_unique(value, **kwargs):
    """
    Validator for unique occurrence in the table, a note here the query is only applicable for DynamoDB and using the
    hash key to look for the uniqueness of the value.

    :param value: str
    :param kwargs: obj
    :return: bool
    """

    module, kls = kwargs.get('params')[0].split('.')

    model = get_class("src.blueprints.{}.models.{}".format(module, kls))
    return model.count(value) == 0


def validate_exists(value, **kwargs):
    """
    Validator for unique occurrence in the table, a note here the query is only applicable for DynamoDB and using the
    hash key to look for the value.

    :param value: str
    :param kwargs: obj
    :return: bool
    """
    module, kls = kwargs.get('params')[0].split('.')

    model = get_class("src.blueprints.{}.models.{}".format(module, kls))

    if not value:
        return True

    return model.count(value) != 0


def validate_date_format(value, params, **kwargs):
    date_format = params[0]
    try:
        datetime.strptime(value, date_format).date()
        return True
    except ValueError:
        return False


class BaseRequest(FormRequest):
    def custom_handlers(self):
        return [{
            'handler': validate_unique,
            'message': 'The :attribute is already being in use',
            'params_count': 0  # the number of parameters the rule expects
        }, {
            'handler': validate_exists,
            'message': 'The :attribute doesn\'t exists',
            'params_count': 0
        },
        {
            'handler': validate_date_format,
            'message': 'Invalid date format.',
            'params_count': 1
        }]