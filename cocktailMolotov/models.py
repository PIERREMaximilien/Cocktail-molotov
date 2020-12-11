# encoding: utf-8
from cocktailMolotov import app, db
from flask import request, jsonify

#from flask_login import UserMixin
import json


# Loop through the ingredients
# change Ingredients -> only rum (ex) or do if ex: rum in ingredients
cocktails = [
    {'id': 0,
    'name': 'mojito',
    'ingredients': ['50 ml White Rum', '8 Mint leaves', '12 1/2 ml Sugar Syrup', '25 ml Lime Juice', '2 Mint sprigs'],
    'description': 'Add the white rum to a highball glass. Add 8 – 10 mint leaves and sugar syrup and lime juice.Muddle with bar spoon. Add crushed ice and a splash of soda. Mix drink down with bar spoon. Taste. Top up with more crushed ice. Slap 2 mint sprigs to release essence and put into drink. Add small splash of soda and straw.'},
    {'id': 1,
    'name': 'martini',
    'ingredients': ['50 ml Gin', '10 ml Dry Vermouth', 'Lemon twist'],
    'description': 'Chill martini glass with soda water and ice. Fill mixing glass to top with ice. Add the dry vermouth to the mixing glass, giving a small stir to coat the ice with the vermouth. Drain out glass, leaving just the coating on the ice. Add the gin to the mixing glass. Stir for 15 seconds, always making sure that the glass is full to the brim with ice. Taste. Fine strain into chilled martini glass. Zest with lemon peel and add twist unto drink.'}
]




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

@app.route('/api/v1/ressources/cocktails/all', methods=['GET'])
def api_all():
    return jsonify(cocktails)



if __name__ == "__main__":
    app.run(debug=True)


