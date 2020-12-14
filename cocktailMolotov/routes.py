import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from cocktailMolotov.forms import RegistrationForm, LoginForm
from cocktailMolotov.models import User
from cocktailMolotov import app, db
from flask_login import login_user, current_user, logout_user, login_required


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
    return jsonify(cocktails)

'''

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
'''