# encoding: utf-8
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from cocktailMolotov import db, login_manager, app
from flask_login import UserMixin
import json


@login_manager.user_loader
def load_user(id):
    return User.objects(id=id).first()

class User(db.Document, UserMixin):
    username = db.StringField(max_length=120, unique=True, required=True)
    email = db.StringField(max_length=120, unique=True, required=True)
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
