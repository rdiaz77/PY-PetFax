# Remember, creating a new blueprint instance requires three arguments:
# The name of the blueprint. Let's name ours pet.
# The location of the blueprint. We can just use the handy __name__.
# The URL prefix that should be used for all routes attached to this blueprint. Let's go with /pets.

# imported render template in addition to Blueprint to render data into the index.html file
from flask import (Blueprint, render_template)
import json # to be able to open the pets.json file

pets = json.load(open('pets.json')) # here we save the json package to a var called "pets" and used open() to open the file. This is a built-in function. And we used json.load() to decode JSON. This is why we had to import the json package. Notice that the json file is passes as str
print(pets)

# new instance of Blueprint
bp = Blueprint ("pet", __name__, url_prefix="/pets" ) 

# add index route

@bp.route('/')
def index():
    return render_template("index.html", pets = pets) # here I called the render_template() and passed the index.html file, so it renders what is in the index.html file. The additional variables, name and values, are passed w/o ""




#now I need to register this route in the __init_py (factory) instance

