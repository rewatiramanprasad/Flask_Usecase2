from werkzeug.exceptions import HTTPException
from flask import Blueprint

flask_blue=Blueprint('errors',__name__)

def page_not_found(e):
    status_code = 500
    if isinstance(e, HTTPException):
        status_code = 404

    response = {
        'success': False,
        'data': {},
        'msg': str(e)
    }

    return response,status_code