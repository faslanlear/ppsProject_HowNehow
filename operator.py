import json
from services import *
from flask import Flask
from werkzeug.exceptions import HTTPException, NotFound


app = Flask(__name__)


@app.route("/operatorcp/acceptroute", methods=['GET'])
def acceptroute():
    return 1
    
@app.route("/operatorcp/breakcall", methods=['GET'])
def breakcall():
    raise NotImplementedError()
    
@app.route("/operatorcp/rejectproblem", methods=['GET'])
def rejectproblem():
    self.app.get('/managercp/route_OP')
    
@app.route("/operatorcp/startcall", methods=['GET'])
def startcall():
    raise NotImplementedError()