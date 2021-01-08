from rest_framework.settings import api_settings


def success_response(data=None, msg='Operation Success'):
    return {
        'success': True,
        'message': msg,
        'data': data
    }


def failure_response(errors, msg='Operation Failure'):
    return {
        'success': False,
        'message': msg,
        'errors': errors
    }
