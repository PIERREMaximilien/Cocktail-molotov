import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from cocktailMolotov.forms import RegistrationForm, LoginForm
from cocktailMolotov.models import User
from cocktailMolotov import app, db
from flask_login import login_user, current_user, logout_user, login_required
from cocktailMolotov import cocktails as api
import requests
from cocktailMolotov.cocktails import cocktails as api
from termcolor import colored

#URL = 'http://127.0.0.1:2000/api/v1/ressources/cocktails/all'
#price = str(requests.request("GET", url, headers=headers, params = querystring).json()['Quotes'][0]['MinPrice'])

@app.route('/')
@app.route('/home')
def home():
    alcohol = request.args.get('alcohol')
    results = []
    if alcohol:
        for x in range(100):
            for alc in api[x]['alcohols']:
                if alc.lower() == alcohol.lower():
                    results.append(api[x])
        return render_template('home.html', title='Home', results=results, alcohol=alcohol)
    return render_template('home.html', title="Home")


@app.route('/mycocktails')
def mycocktails():
    return render_template('myCocktails.html', title='My Cocktails')


@app.route('/singlecocktail')
def singlecocktail():
    return render_template('singlecocktail.html')


@app.route('/profile')
def profile():
    return render_template('profile.html', title='My Profile')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    '''
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    '''
    if form.validate_on_submit():
        #hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        user.save()
        flash(f'Thanks {form.username.data}! Your account has been created, you are now able to log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    '''
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()

        if user.password == form.password.data:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/api/v1/ressources/cocktails/all', methods=['GET'])
def api_all():
    return redirect(url_for('my_cocktail'))
    result = []
    string = ''
    for x in range(100):
        for alcohol in api.cocktails[x]['alcohols']:
            if alcohol == 'absinthe':
                result.append(api.cocktails[x])
        #result += api.cocktails[x]['alcohols'][0]
    print(result)
    #return 'OK'
    return jsonify(result)