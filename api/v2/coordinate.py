from flask import Blueprint

coordinate = Blueprint('v2', __name__)


@coordinate.route('/coordinate')
def get_cordinate():
    return {'Hello': 'Coordinate'}