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
    return render_template('allCocktails.html', title='All cocktails')

@app.route('/mycocktails')
def mycocktails():
    return render_template('myCocktails.html', title='My cocktails')