# encoding: utf-8
from flask import request, jsonify
from cocktailMolotov import app, db
from flask_mongoengine import MongoEngine#, StringField, IntField

#from flask_login import UserMixin
import json




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





