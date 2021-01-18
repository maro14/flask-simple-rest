from flask import Blueprint

cordinate = Blueprint('v2', __name__)


@cordinate.route('/cordinate')
def get_cordinate():
    return {'Hello': 'Cordinate'}