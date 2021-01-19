from flask import Blueprint, jsonify
from api.db.route import ROUTE

location = Blueprint('v1', __name__)

@location.route('/location', methods=["GET"])
def get_location():
    return jsonify({'location': ROUTE})


@location.route('/location/<name_route>')
def get_name(name_route):
    name_found = [
        name for name in ROUTE if name['name'] == name_route]
    if (len(name_found) > 0):
        return jsonify({'name': name_found[0]})
    return jsonify({'massage': 'Name not found'})