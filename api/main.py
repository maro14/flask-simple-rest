from flask import Blueprint, Flask
from api.v1.location import get_location
from api.v2.cordinate import cordinate


app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return{'Welcome': 'To my restapi'}

app.register_blueprint(cordinate, url_prefix='/v2')
app.add_url_rule('/v1/location', 'location', get_location)
