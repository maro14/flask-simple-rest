from flask import Blueprint, jsonify
from api.db.route import ROUTE

coordinate = Blueprint('v2', __name__)


@coordinate.route('/coordinate')
def get_cordinate():
    return jsonify(ROUTE)

@coordinate.route('/coordinate/<lat>')
def get_lag(lat):
    the_coordinate = [
        lat for lat in ROUTE if lat['lat'] == lat
    ]
    return {'latitude': the_coordinate[0]}