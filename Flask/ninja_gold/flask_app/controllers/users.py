from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request
import random
# Create Users Controller

def calculate_gold(action):
    if action == 'farm':
        min_gold = 10
        max_gold = 20
        return random.randint(min_gold, max_gold)
    elif action == 'cave':
        min_gold = 5
        max_gold = 10
        return random.randint(min_gold, max_gold)
    elif action == 'house':
        min_gold = 2
        max_gold = 5
        return random.randint(min_gold, max_gold)
    elif action == 'casino':
        min_gold = -50
        max_gold = 50
        return random.randint(min_gold, max_gold)
    else:
        return 0
# Read Users Controller

@app.route('/')
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0
    if 'console_log' not in session:
        session['console_log'] = []

    total_gold = session['total_gold']
    console_log = session['console_log']

    return render_template('index.html', total_gold=total_gold, console_log=console_log)

@app.route('/process_money', methods=['POST'])
def process_money():
    action = request.form['action']
    gold_earned = calculate_gold(action)

    total_gold = session['total_gold']
    console_log = session['console_log']

    total_gold += gold_earned
    console_log.append(f"You {action} {gold_earned} gold")

    session['total_gold'] = total_gold
    session['console_log'] = console_log
    return redirect('/')

# Update Users Controller



# Delete Users Controller


# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')                                   The variable must be in the path within angle brackets
# def index(id):                                            It must also be passed into the function as an argument/parameter
#     user_info = user.User.get_user_by_id(id)              The it will be able to be used within the function for that route
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.

# Render template is a function that takes in a template name in the form of a string, then any number of named arguments containing data to pass to that template where it will be integrated via the use of jinja
# Redirect redirects from one route to another, this should always be done following a form submission. Don't render on a form submission.