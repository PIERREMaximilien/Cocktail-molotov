import os
from flask import Flask
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

app = Flask(__name__)


app.config['SECRET_KEY'] = '54cb0a1257b1585952f7ea15492dc6fa'
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

PASSWORD = 'ok'
USERNAME = 'AlexPY6'
DB_NAME = 'Cocktail-Molotov'
DB_URI = f'mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.f9xlu.mongodb.net/{DB_NAME}?retryWrites=true&w=majority'
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine(app)


from cocktailMolotov import routes
