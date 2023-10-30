from flask import Flask
app = Flask(__name__)
app.secret_key = "3b4a6e0e1079f71cf2c0a3e4c1e17a19" 

# The secret key is needed to run session
# This is one thing that would usually be kept in your git ignore, along with API keys