from flask_app import app
import random
from flask import render_template, redirect, request, session, url_for
from flask_app.models import user # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

# Create Users Controller



# Read Users Controller

@app.route('/')
def index():
    if 'random_number' not in session:
        session['random_number'] = random.randint(1, 100)

    if 'message' not in session:
        session['message'] = "I am thinking of a number 1 through 100....."

    message = session['message']
    return render_template('index.html', message=message)

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['guess'])
    random_number = session['random_number']

    if user_guess == random_number:
        session['message'] = "You are correct!"
        message_color = "text-success"
    elif user_guess < random_number:
        session['message'] = "Too low! Try again"
        message_color = "text-danger"
    else:
        session['message'] = "Too high! Try again"
        message_color = "text-warning"

    return redirect(url_for('index', message=session['message'], message_color=message_color))

@app.route('/restart', methods=['POST'])
def restart():
    session.pop('random_number', None)
    session.pop('message', None)
    return redirect(url_for('index'))


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