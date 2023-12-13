import json
from services import *
from flask import Flask
from werkzeug.exceptions import HTTPException, NotFound


app = Flask(__name__)


@app.route("/ai/recognise", methods=['GET'])
def recognise():
    raise NotImplementedError()
    
@app.route("/ai/train", methods=['GET'])
def train():
    raise NotImplementedError()