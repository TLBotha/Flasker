from flask import Flask, render_template
from pkg_resources import safe_extra

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

#def index():
 #   return "<h1>Hello World!</h1>"

#FILTERS!!!!

 #safe
 #capitalize
 #lower
 #upper
 #title
 #trim (remove trailing spaces)
 #striptags

def index():
    first_name = "John"
    stuff_safe_striptags = "This is <strong>bold</strong>"
    stuff = "this is bold"

    favorite_pizza = ["Peperoni", "Cheese", "Mushroom", 41]
    
    return render_template("index.html", first_name=first_name, stuff=stuff , stuff_safe_striptags=stuff_safe_striptags, favorite_pizza=favorite_pizza)

# localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def Internal_Server_Error(e):
    return render_template("500.html"), 500