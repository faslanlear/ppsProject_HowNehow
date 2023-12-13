import json
from services import *
from flask import Flask
from werkzeug.exceptions import HTTPException, NotFound
from collections import deque

app = Flask(__name__)

q = deque()

@app.route("/queue/push_back/<element>", methods=['GET'])
def push_back(element):
    q.append(element)

@app.route("/queue/pop/", methods=['GET'])
def pop():
    return q.pop()

@app.route("/queue/push_back/<element>/<position>", methods=['GET'])
def insert(element, position):
    q.insert(element, position)
    
@app.route("/queue/remove/<position>", methods=['GET'])
def remove(position):
    q.remove(position)