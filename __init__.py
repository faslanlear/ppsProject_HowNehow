import os
import json
from flask import Flask
from flask import make_response


def root_dir():
    return os.path.dirname(os.path.realpath(__file__ + '/..'))
