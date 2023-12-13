import json
from services import *
from flask import Flask
from werkzeug.exceptions import HTTPException, NotFound


app = Flask(__name__)


@app.route("/callhandler/accept_call", methods=['GET'])
def accept_call():
    call_menu(1)
    
@app.route("/callhandler/break_call", methods=['GET'])
def break_call():
    raise NotImplementedError()
    
@app.route("/callhandler/call_menu", methods=['GET'])
def call_menu(number):
    if number == 1:
        ask_for_ai_route()
    if number == 2:
        option = get_button()
        if option == 1:
            Enquire()
        if option == 2:
            CallOperator()
        if option == 3:
            ThemedCall()    
    
@app.route("/callhandler/routing", methods=['GET'])
def routing(id):
    raise NotImplementedError()
 
@app.route("/callhandler/ask_for_ai_route", methods=['GET'])
def ask_for_ai_route():
    result = self.app.get('/managercp/route_AI')
    if result == 1:
        question = receive()
        answer = self.app.get('/managercp/accept_routing/{}'.format(question))
        TTS(answer)
        client_answer = get_button()
        if client_answer == 0:
            call_menu(2)

@app.route("/callhandler/ask_for_op_route", methods=['GET'])
def ask_for_op_route():
    self.app.get('/managercp/route_OP')
            
@app.route("/callhandler/get_button", methods=['GET'])
def get_button():
    raise NotImplementedError()
    
@app.route("/callhandler/receive", methods=['GET'])
def receive():
    raise NotImplementedError()
    

@app.route("/selectmenu/enquire", methods=['GET'])
def Enquire():
    self.app.get('/queue/push_back/{}'.format(number + "|" + str(time.time()) + "|" + "Enquire"))
    
@app.route("/selectmenu/calloperator", methods=['GET'])
def CallOperator():
    self.app.get('/queue/push_back/{}'.format(number + "|" + str(time.time()) + "|" + "None"))
    
@app.route("/selectmenu/themedcall", methods=['GET'])
def ThemedCall():
    theme = get_button()
    self.app.get('/queue/push_back/{}'.format(number + "|" + str(time.time()) + "|" + str(theme)))
    