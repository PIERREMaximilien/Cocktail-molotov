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
    'name': 'Mojito',
    'ingredients': ['50 ml White Rum', '8 Mint leaves', '12 1/2 ml Sugar Syrup', '25 ml Lime Juice', '2 Mint sprigs'],
    'description': 'Add the white rum to a highball glass. Add 8 – 10 mint leaves and sugar syrup and lime juice.Muddle with bar spoon. Add crushed ice and a splash of soda. Mix drink down with bar spoon. Taste. Top up with more crushed ice. Slap 2 mint sprigs to release essence and put into drink. Add small splash of soda and straw.'},
    {'id': 1,
    'name': 'Martini',
    'ingredients': ['50 ml Gin', '10 ml Dry Vermouth', 'Lemon twist'],
    'description': 'Chill martini glass with soda water and ice. Fill mixing glass to top with ice. Add the dry vermouth to the mixing glass, giving a small stir to coat the ice with the vermouth. Drain out glass, leaving just the coating on the ice. Add the gin to the mixing glass. Stir for 15 seconds, always making sure that the glass is full to the brim with ice. Taste. Fine strain into chilled martini glass. Zest with lemon peel and add twist unto drink.'},
    {'id': 2,
    'name': 'Daiquiri',
    'ingredients': ['50 ml White Rum', '1/2 bar spoons Sugar', '25 ml Lime Juice', 'Lime slice'],
    'description': 'Chill coupe glass with soda water. Add sugar to mixing tin and then add white rum and lime juice. Add a little cracked ice to the bottom then fill the rest of the tin with ice. Shake for 10 – 15 seconds, taste and then fine strain into coupe glass. Garnish glass with lime slice.'},
    {'id': 3,
    'name': 'Old Fashioned',
    'ingredients': ['50 ml Bourbon', '2 dashes Angostura Bitters', '1 dash Orange Bitters', '1 bar spoon Sugar', 'Orange peel'],
    'description': 'Begin by chilling rocks glass with ice and soda water. Add 1 bar spoon of sugar into mixing glass. Add 2 dashes of Angostura bitters and 1 dash of orange bitters. Muddle to break down the sugar into a paste. Add the bourbon into a mixing glass and fill the rest of the mixing glass with ice. Stir with bar spoon for at least 20 seconds. Top up with ice and taste. Put ice into rocks glass and strain the drink into the glass. Zest the glass with orange peel and add twist into drink.'},
    {'id': 4,
    'name': 'Cosmopolitan',
    'ingredients': ['1/2 ml Citrus Vodka', '1/2 ml Triple Sec', '30 ml Cranberry Juice', '1/2 squeezed lemon', '1/2 ml Sugar Syrup'],
    'description': 'Chill coupe glass with soda water. Add all ingredients to mixing tin with ice. Shake for 10 to 15 seconds. Fine strain into the chilled coupe glass. Flame an orange peel and place in drink as garnish.'},
    {'id': 5,
    'name': 'Caipirinha',
    'ingredients': ['50 ml Cachaca', '1/2 Lime', '1 teaspoon Brown Sugar', 'Lime Wedge'],
    'description': 'Cut 1/2 lime into 1/8 ths and add half of these to Rocks glass. Add teaspoon of brown sugar and muddle the ingredients. Add the rest of the lime and continue to muddle, to dissolve the sugar. Add the Cachaca and then add crushed ice on top. Stir to continue to dissolve the sugar. Add more crushed ice and continue to stir. Top up with crushed ice and garnish with lime wedge.'},
    {'id': 6,
    'name': 'White Russian',
    'ingredients': ['1/2 ml Vodka', '25 ml Coffee Liqueur', '15 ml Cream', '15 ml Milk', 'Chocolate Powder', 'Coffee Bean'],
    'description': 'For the perfect White Russian recipe add coffee liqueur to an old-fashioned glass. Add other ingredients to mixing tin and fill to brim with ice. Shake for 10 -15 seconds. Single strain the ingredients over the ice and coffee liqueur. Sprinkle with chocolate powder and garnish with coffee bean.'},
    {'id': 7,
    'name': 'Pina Colada',
    'ingredients': ['50 ml White Rum', '100 ml Pineapple Juice', '25 ml Coconut Cream', ' 25 ml Cream', 'Pineapple Slice', 'pinch of Salt'],
    'description' : 'Chill highball glass. Add all ingredients to mixing tin and fill with ice. Shake vigorously for 10 – 15 seconds. Fill highball glass with fresh ice and strain drink into glass. Garnish with pineapple slice, add straw and serve.'},
    {'id': 8,
    'name': 'Negroni',
    'ingredients': ['25 ml Gin', '25 ml Sweet Red Vermouth', '25 ml Campari', 'Orange Peel'],
    'description': 'Chill rocks glass with ice and soda water.Fill mixing tin to rim with ice and add in all ingredients. Stir with bar spoon for 20 seconds. Taste. Add fresh ice to rocks glass and strain the drink into glass. Zest glass with orange peel, twist and place in drink.'},
    {'id': 9,
    'name': 'Bramble',
    'ingredients': ['50 ml Gin', '10 ml Crème de Mure', '25 ml Lemon Juice', '1/2 ml Sugar Syrup', 'Blackberry'],
    'description': 'Add all ingredients (except creme de mure) into mixing glass. Fill  mixing glass with cubed ice and fill rocks glass with crushed ice. Shake for 10 seconds. Strain mixture into glass and top up with crushed ice. Pour creme de mure over drink using bar spoon. Garnish with 2 lemon slices and blackberry.'},
    {'id': 10,
    'name': 'Margarita',
    'ingredients': ['1/2 ml Tequila', '1/2 ml Triple Sec', '25 ml Lime Juice', '1/2 ml Simple Syrup', 'salt'],
    'description': 'Begin by half soaking rim of coupe glass with lime juice and then dab in salt. Use cloth to tidy up the glass for presentation. Add all ingredients into mixing tin with 2 ice cubes and dry shake for 10 seconds. Fill mixing tin with ice and shake for a further 10 – 15 seconds. Fine strain into the pre-prepared coupe glass.'},
    {'id': 11,
    'name': 'Dark and Stormy',
    'ingredients': ['50 ml Dark Rum', '4 Lime quarters', '1/2 bar spoons Brown Sugar', 'splash Ginger Beer', 'Lime wedge'],
    'description': 'Chill highball glass with soda water. Place 4 lime quarters into mixing tin and add 1 1/2 bar spoons of brown sugar. Muddle ingredients. Add 50 ml of dark rum. Fill mixing tin with ice and shake hard for 10 – 15 seconds. Taste. Add fresh ice to the highball glass and single strain drink over the ice. Top up with ginger beer and add straw. Garnish with lime wedge.'},
    {'id': 12,
    'name': 'Cuba Libre',
    'ingredients': ['50 ml Anejo Rum', '8 Lime wedges', '100 ml Cola', 'Lime wedge'],
    'description': 'Add rum into rocks glass and squeeze the lime wedges over the top. Give quick churn with bar spoon and top up with ice. Fill to brim with cola and add in lime wedge as garnish.'},
    {'id': 13,
    'name': 'Sazerac',
    'ingredients': ['50 ml Rye Whiskey', '5 ml Absinthe', ' 3 dashes of Peychauds Bitters', 'Sugar Cube', 'Lemon Peel'],
    'description': 'One rocks glass is packed with ice and water to chill the glass. In a second rocks glass, muddle the sugar cube with the bitters. Add the rye to this mixture. Stir to combine. Empty the ice from the first glass. Pour the absinthe into the glass and swirl to coat the sides of the glass. Any excess absinthe is discarded. Pour the rye/sugar/bitters mixture into the coated glass. Twist a lemon peel over the glass and rub the rim of the glass with the peel. The peel can be discarded or placed in the cocktail.'},
    {'id': 14,
    'name': 'Bloody Mary',
    'ingredients': ['1/2 ml Peppered Vodka', '15 ml Sweet Vermouth', '35 ml Tomato Juice', 'splash Red Wine', '6 splashes Worcestershire sauce', '10 dashes Tobasco sauce', ' 25 ml Lemon Juice', '10 dashes Salt', '10 dashes Pepper', '3 Cucumber slices'],
    'description': 'Chill a highball glass with ice. Pour all the ingredients, apart from red wine, into mixing tin and add ice. Roll the mixing tin for 15 seconds. Taste. Add ice to glass and single strain the drink into a glass. Add  a splash of red wine and a dash of pepper. Garnish with 3 cucumber slices.'},
    {'id': 15,
    'name': 'Manhattan',
    'ingredients': ['50 ml Bourbon', '10 ml Sweet Vermouth', '10 ml Dry Vermouth', '2 dashes Angostura Bitters', 'Orange peel'],
    'description': 'Chill cocktail glass with ice and soda. Fill a mixing glass with ice and then add all ingredients. Using a bar spoon, stir the drink for approximately 20 seconds. When stirring, always ensure the glass is topped up with ice.Taste and then strain into the chilled cocktail glass, serving straight up. Zest the drink and glass with the orange peel and then twist and place in glass.'},
    {'id': 16,
    'name': 'Long Island Iced Tea',
    'ingredients': ['15 ml Gin', '15 ml Vodka', '15 ml Tequila', '15 ml White Rum', '15 ml Triple Sec', '25 ml Lemon Juice', '30 ml Gomme syrup', 'splash of Cola'],
    'description': 'Begin by chilling highball glass with soda water and ice. Add all ingredients (except the cola) into a mixing tin. Add ice to tin and shake for 10 seconds. Add fresh ice to highball glass and add splash of cola. Strain the ingredients into glass. Add lemon slice and straw.'},
    {'id': 17,
    'name': 'Mai-Tai',
    'ingredients': ['20 ml Dark Rum', '20 ml Light Rum', 'splash Demerara 20 ml Triple Sec', '20 ml Lime Juice', '10 ml Orgeat Syrup', 'Mint sprig', 'Orange wedge'],
    'description': 'Add all ingredients into mixing tin. Fill mixing tin with cubed ice. Shake very hard for 10 seconds to achieve desired dilution. Fill goblet style glass with crushed ice and strain mixture into glass. Add a short straw, mint and a splash of demerara rum.'},
    {'id': 18,
    'name': 'Amaretto Sour',
    'ingredients': ['50 ml Amaretto', '25 ml Lemon Juice', '1/2 ml Simple Syrup', 'dash Egg-White', 'dash Angostura Bitters', 'Lemon Zest'],
    'description': 'Add all ingredients into mixing glass. Dry shake for 5 seconds. Add cubed ice into shaker and shake for 10 seconds. Fill rocks glass with cubed ice and strain mixture into glass. Garnish with lemon zest, spreading the oils across the glass.'},
    {'id': 19,
    'name': 'Singapore Sling',
    'ingredients': ['1/2 ml Gin', '1/2 ml Cherry Heering', '1/2 ml Benedictine', '25 ml Lemon Juice', '2 dashes Orange Bitters', '2 dashes Angostura Bitters', 'dash Soda Water', 'Lemon slice'],
    'description': 'Chill highball glass with soda water. Add all ingredients into mixing tin and fill with ice. Shake hard for 10 seconds. Taste. Top up the highball glass with ice and single strain the drink into glass. Top up with soda water, add straw and garnish with lemon slice.'},
    {'id': 20,
    'name': 'French Martini',
    'ingredients': ['25 ml Vodka', '25 ml Chambord', '75 ml Pineapple Juice', '3 Raspberries for Garnish'],
    'description': 'Pour the ingredients into a cocktail shaker with ice cubes, shake well, Strain into a chilled cocktail glass, arnish with 3 Raspberries.'},
    {'id': 21,
    'name': 'Espresso Martini',
    'ingredients': ['1/2 ml Vanilla Vodka', '1/2 ml Kahlúa', 'Double Espresso', '1/2 ml Sugar Syrup', '3 Coffee Beans'],
    'description': 'Add all ingredients into a Boston cocktail shaker and fill with ice. Shake hard for up to 30 seconds to achieve the desired consistency of the drink. Double strain the contents of the shaker into a chilled martini glass. Garnish with 3 coffee beans.'},
    {'id': 22,
    'name': 'Strawberry Daiquiri',
    'ingredients': ['1/2 ml Bacardi Rum', '1/2 ml Strawberry Liqueur', '25 ml Lime Juice', '1/2 ml Sugar Syrup', '1 Strawberry'],
    'description': 'Add all ingredients into a Boston Shaker and fill with ice. Shake for about 15 seconds and then strain into a chilled martini glass. Garnish with a strawberry.'},
    {'id': 23,
    'name': 'Moscow Mule',
    'ingredients': ['1/2 ml Vodka', '25 ml Lime juice', '1/2 ml Sugar Syrup', 'splash Ginger Beer'],
    'description': 'Chill highball glass with ice and soda. Add all ingredients apart from ginger beer into mixing tin. Fill tin with ice and shake for about 10 – 15 seconds. Fill glass with fresh ice. Add splash of ginger beer to bottom of glass and strain drink into glass. Add straw and garnish with lime wedge.'},
    {'id': 24,
    'name': 'Clover Club',
    'ingredients': ['1/2 ml Caorunn Gin', '1/2 ml Lemon Juice', '20 ml Sweet Vermouth', '20 ml Raspberry Syrup', '1 Egg White'],
    'description': 'Pour the ingredients into cocktail shaker and dry shake for 5 seconds. Add ice to the shaker and shake hard for a further 15 seconds. Single strain into a coupe glass and serve.'},
    {'id': 25,
    'name': 'Mint Julep',
    'ingredients': ['50 ml Knob Creek Bourbon', 'bar spoon Granulated Sugar', '8 Mint leaves', 'Mint sprigs'],
    'description': 'Add a bar spoon of granulated sugar into glass. Place 8 mint leaves into the glass and add 15 ml of Bourbon. Gently muddle contents of the glass. Add a further 35 ml of bourbon and then fill glass half way with crushed ice. Churn for 15 seconds and taste. Fill the remainder of the glass to the top with crushed ice. Slap mint sprigs to release flavour and add to top of drink. Place straw into drink next to mint sprigs.'},
    {'id': ,
    'name': '',
    'ingredients': [''],
    'description': ''},
    {'id': ,
    'name': '',
    'ingredients': [''],
    'description': ''},
    {'id': ,
    'name': '',
    'ingredients': [''],
    'description': ''},
    {'id': ,
    'name': '',
    'ingredients': [''],
    'description': ''},
    {'id': ,
    'name': '',
    'ingredients': [''],
    'description': ''},
    {'id': ,
    'name': '',
    'ingredients': [''],
    'description': ''},
    {'id': ,
    'name': '',
    'ingredients': [''],
    'description': ''},
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
