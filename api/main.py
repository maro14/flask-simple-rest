from flask import Blueprint, Flask
from api.v1.location import location
from api.v2.coordinate import coordinate


app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return{'Welcome': 'To my restapi'}

app.register_blueprint(coordinate, url_prefix='/v2')
app.register_blueprint(location, url_prefix='/v1')
