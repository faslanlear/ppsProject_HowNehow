import json
from services import *
from flask import Flask
from werkzeug.exceptions import HTTPException, NotFound


app = Flask(__name__)


@app.route("/managercp/route_AI", methods=['GET'])
def route_AI():
    return 1
    
@app.route("/managercp/route_OP", methods=['GET'])
def route_OP():
    return self.app.get('/operator/acceptroute')
    
@app.route("/managercp/train", methods=['GET'])
def train():
    self.app.get('/AI/train')
    
@app.route("/managercp/view_queue", methods=['GET'])
def view_queue():
    raise NotImplementedError()