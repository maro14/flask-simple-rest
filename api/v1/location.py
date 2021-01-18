from flask import jsonify
from api.db.location import locations

def get_location():
    return jsonify({'location': locations})