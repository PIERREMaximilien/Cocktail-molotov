import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from cocktailMolotov.forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm
from cocktailMolotov.models import User
from cocktailMolotov.models import Cocktail
from cocktailMolotov import app, db, mail
from flask_login import login_user, current_user, logout_user, login_required
from cocktailMolotov.cocktails import cocktails as api
from flask_mail import Message

#URL = 'http://127.0.0.1:2000/api/v1/ressources/cocktails/all'
#price = str(requests.request("GET", url, headers=headers, params = querystring).json()['Quotes'][0]['MinPrice'])

@app.route('/')
@app.route('/home')
def home():
    alcohol = request.args.get('alcohol')
    results = []
    results_fav = [api[4], api[9], api[15]]
    if alcohol:
        for x in range(len(api)):
            for alc in api[x]['alcohols']:
                if alc.lower() == alcohol.lower():
                    results.append(api[x])
        return render_template('home.html', title='Home', results=results, alcohol=alcohol)
    else:
        return render_template('home.html', title='Home', results_fav=results_fav)
    return render_template('home.html', title="Home")
    


@app.route('/mycocktails')
def mycocktails():
    return render_template('myCocktails.html', title='My Cocktails')


@app.route('/singlecocktail')
def singlecocktail():
    name = request.args.get('name')
    description = request.args.get('description')
    ingredients = request.args.get('ingredients')[1:-1].replace('\'', '').split(',')
    return render_template('singlecocktail.html', title=name, name=name, description=description, ingredients=ingredients)


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
    return redirect(url_for('home', title='Home'))


def send_reset_email(user):
    msg = Message('Password Reset Request', sender='cocktail.molotov.info@gmail.com', recipients=[user.email])
    msg.body = f'''Please visit this link to reset your password:
    {url_for('reset_token', _external=True)}
    '''
    mail.send(msg)

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    form = RequestResetForm()
    
    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent to your email address.')
        return redirect(url_for('login'))
    
    return render_template('reset-request.html', title='Reset Password', form=form)

@app.route('/reset_token', methods=['GET', 'POST'])
def reset_token():
    form = ResetPasswordForm()

    if form.validate_on_submit():
        User.objects(email=form.email.data).update(password = form.password.data)
        flash('Your password has been updated')

    return render_template('reset-token.html', title='Reset Password', form=form)


@app.route('/add/favorites/<name>', methods=['GET'])
def favorites(name):
    cocktail_name = str(name)
    if current_user:
        if Cocktail.objects(name=cocktail_name, user_id=current_user.id).first():
            flash('You already have it in your favorites.', 'error')
            return redirect(url_for('favorite_cocktails'))
        else:
            cocktail = Cocktail(name=cocktail_name, user_id=str(current_user.id))
            cocktail.save()
            flash('Added to your favorites.')
            return redirect(url_for('favorite_cocktails'))
    else:
        flash('You need to log in first.', 'success')
        return redirect(url_for('login'))


@app.route('/favorite-cocktails', methods=['GET'])
def favorite_cocktails():
    results = []
    favorites = Cocktail.objects(user_id=str(current_user.id))
    favorite_names = [x.name.lower() for x in favorites]
    for x in range(len(api)):
        if str(api[x]['name'].lower()) in favorite_names:
            results.append(api[x])

    return render_template('favorites.html', title="Favorites", results=results)

'''
alcohol = request.args.get('alcohol')
    results = []
    results_fav = [api[4], api[9], api[15]]
    if alcohol:
        for x in range(len(api)):
            for alc in api[x]['alcohols']:
                if alc.lower() == alcohol.lower():
                    results.append(api[x])
        return render_template('home.html', title='Home', results=results, alcohol=alcohol)
    else:'''
"""
THIS WAS JUST DUMB
@app.route('/add/favorites/<name>', methods=['GET'])
def favorites(name):
    #return current_user.cocktails 
    if current_user:
        cocktail_name = str(name)
        current_user.cocktails += cocktail_name
        cocktail_list = str(current_user.cocktails += cocktail_name).split(',')
        #return str(current_user.cocktails)

        return str(current_user.cocktails.split(','))
        if cocktail_name not in cocktail_list:
            print(cocktail_name)
            print('in IT')
            new_cocktail_list = cocktail_list.append(cocktail_name)
            print(new_cocktail_list)
            return str(new_cocktail_list)
            ''User.objects(id=current_user.id).update(cocktails = current_user.cocktails.append(cocktail_name))
            flash('Added to favorites', 'success')
            # We can do it with a string and always split and get a list like this.
        else:
            flash('You already have it in your favorites', 'error')
        return str(current_user.cocktails)'''
        #return cocktail_name
    else:
        flash('You need to login first.', 'success')
        return redirect(url_for('login'))

#user = User.objects(email=form.email.data).first()
"""