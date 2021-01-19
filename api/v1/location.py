from flask import Blueprint, jsonify
from api.db.location import locations

location = Blueprint('v1', __name__)

@location.route('/location')
def get_location():
    return jsonify({'location': locations})