#!/usr/bin/python3
"""Start a flask web app
"""

from flask import Flask
app = Flask(__name__)

<<<<<<< HEAD
<<<<<<< HEAD
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

def hello hbnb():
"""
Displays 'Hello HBNB!'
"""
return "Hello HBNB!"

if _name_ === "_main_":
>>>>>>> f6bf04063aa69be27b1e761fe97601dc17c8e3ff

# Start the Flask development server

# Listen on all available network interfaces (0.0.0.0) and port 5000
app.run(host='0.0.0.0', port=5000)
=======
# Define the route for the root URL '/'
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!'
=======

@app.route('/')
def hello_flask():
    """Return string when route queried
>>>>>>> 5cff9cdd6b7a4de7d997ac2941e4603a12e8df98
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 858dcbfbd990ef9a145d78db078875955e4ec55d
