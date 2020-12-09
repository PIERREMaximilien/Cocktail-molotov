# encoding: utf-8
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from datetime import datetime
#from cocktailMolotov import login_manager, app
#from flask_login import UserMixin
import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'Cocktail-Molotov',
    'host': 'localhost',
    'port': 27017
}
#app.config['MONGODB_DB'] = 'Cocktail-Molotov'
#app.config['MONGODB_HOST'] = '192.168.1.35'
#app.config['MONGODB_PORT'] = 12345
#app.config['MONGODB_USERNAME'] = 'webapp'
#app.config['MONGODB_PASSWORD'] = 'pwd123'
db = MongoEngine()
db.init_app(app)

class User(db.Document):
    user_id = db.IntField(primary_key=True)
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


if __name__ == "__main__":
    app.run(debug=True)



'''
from datetime import datetime
from cocktailMolotov import login_manager, app
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default-pic.jpeg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)


class Cocktail(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default-cocktail.jpeg')
    description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)




class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "email": self.email}'''

'''

import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "email": self.email}

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    user = User.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    user = User(name=record['name'],
                email=record['email'])
    user.save()
    return jsonify(user.to_json())

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(email=record['email'])
    return jsonify(user.to_json())

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())

if __name__ == "__main__":
    app.run(debug=True)
'''