#!/usr/bin/python3

"""Starts a Flask web application.

from flask import Flask

app = Flask (_name_)

<<<<<<< HEAD
# Define the route for route URL '/'
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!'
    """
    return "Hello HBNB!"
=======
#Define the route for the root URL '/'
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello hbnb ():
""" Displays 'Hello HBNB! """
return "Hello HBNB!"

if _name_ === "_main_":
>>>>>>> f6bf04063aa69be27b1e761fe97601dc17c8e3ff

# Start the Flask development server

# Listen on all available network interfaces (0.0.0.0) and port 5000
app.run(host='0.0.0.0', port=5000)
