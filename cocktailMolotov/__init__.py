import os
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

from cocktailMolotov import routes
