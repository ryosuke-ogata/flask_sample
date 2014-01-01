# -*- coding: utf-8 -*-
import sys,os

FLASK_APP_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(FLASK_APP_DIR)
# Flask
from flask import Flask
flask = Flask(__name__)

# Log
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
    datefmt='%Y%m%d-%H:%M%p',
)

# Controller
from controller.root import app as rootApp
flask.register_blueprint(rootApp)
from controller.upload import app as uploadApp
flask.register_blueprint(uploadApp)
