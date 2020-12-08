import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from cocktailMolotov import app


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

@app.route('/profile')
def profile():
    return render_template('profile.html', title='My Profile')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

