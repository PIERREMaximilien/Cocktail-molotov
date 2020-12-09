import os
from flask import Flask, request, jsonify
from flask_login import LoginManager

app = Flask(__name__)


from cocktailMolotov import routes
