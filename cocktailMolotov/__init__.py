import os
from flask import Flask
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

app = Flask(__name__)


PASSWORD = 'ok'
USERNAME = 'AlexPY6'
DB_NAME = 'Cocktail-Molotov'
DB_URI = f'mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.f9xlu.mongodb.net/{DB_NAME}?retryWrites=true&w=majority'
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine(app)


from cocktailMolotov import routes
