# encoding: utf-8
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine#, StringField, IntField
from cocktailMolotov import app
#from flask_login import UserMixin
import json


# ! WE NEED TO ADD GITIGNORE
PASSWORD = 'ok'
USERNAME = 'AlexPY6'
DB_NAME = 'Cocktail-Molotov'
DB_URI = f'mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.f9xlu.mongodb.net/{DB_NAME}?retryWrites=true&w=majority'
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine(app)

class User(db.Document):
    #user_id = db.IntField(primary_key=True)
    username = db.StringField(max_length=120, unique=True, required=True)
    email = db.StringField(max_length=120, unique=True, required=True)
    #image_file = db.StringField(default='default-pic.jpeg')
    password = db.StringField(max_length=120, unique=True, required=True)

class Cocktail(db.Document):
    cocktail_id = db.IntField(primary_key=True)
    name = db.StringField(max_length=120, unique=True, required=True)
    image_file = db.StringField(default='default-cocktail.jpeg')
    description = db.StringField()
    ingredients = db.StringField()

@app.route('/add', methods=['GET'])
def db_test():
    test = User(username='test', email='test@gmail.com', password='test').save()
    #user.save()
    return 'Success'

@app.route('/', methods=['GET'])
def test():
    return 'RUN'





'''
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from datetime import datetime
#from cocktailMolotov import login_manager, app
#from flask_login import UserMixin
import json


app = Flask(__name__)

# ! WE NEED TO ADD GITIGNORE
PASSWORD = 'ok'
USERNAME = 'AlexPY6'
DB_NAME = 'Cocktail-Molotov'
DB_URI = f'mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.f9xlu.mongodb.net/{DB_NAME}?retryWrites=true&w=majority'
app.config["MONGODB_HOST"] = DB_URI



db = MongoEngine(app)
#db.init_app(app)

class User(db.Document):
    #user_id = db.IntField(primary_key=True)
    username = db.StringField(max_length=120, unique=True, required=True)
    email = db.StringField(max_length=120, unique=True, required=True)
    #image_file = db.StringField(default='default-pic.jpeg')
    password = db.StringField(max_length=120, unique=True, required=True)

class Cocktail(db.Document):
    cocktail_id = db.IntField(primary_key=True)
    name = db.StringField(max_length=120, unique=True, required=True)
    image_file = db.StringField(default='default-cocktail.jpeg')
    description = db.StringField()
    ingredients = db.StringField()

@app.route('/add', methods=['GET'])
def db_test():
    test = User(username='test', email='test@gmail.com', password='test').save()
    #user.save()
    return 'Success'

@app.route('/', methods=['GET'])
def test():
    return 'RUN'



if __name__ == "__main__":
    app.run(debug=True)
'''