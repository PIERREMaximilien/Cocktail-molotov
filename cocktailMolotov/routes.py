import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from cocktailMolotov import app
from flask import jsonify


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


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")

@app.route('/allcocktails')
def allcocktails():
    return render_template('allCocktails.html', title='All Cocktails')

@app.route('/mycocktails')
def mycocktails():
    return render_template('myCocktails.html', title='My Cocktails')

@app.route('/singlecocktail')
def singlecocktail():
    return render_template('singlecocktail.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', title='My Profile')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/login')
def login():
    return render_template('login.html', title='Log in')

@app.route('/api/v1/ressources/cocktails/all', methods=['GET'])
def api_all():
    return jsonify(cocktails)
