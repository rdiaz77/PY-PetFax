# Remember, creating a new blueprint instance requires three arguments:
# The name of the blueprint. Let's name ours pet.
# The location of the blueprint. We can just use the handy __name__.
# The URL prefix that should be used for all routes attached to this blueprint. Let's go with /pets.

# imported render template in addition to Blueprint to render data into the index.html file
from flask import (Blueprint, render_template)

# new instance of Blueprint
bp = Blueprint ("pet", __name__, url_prefix="/pets" ) 

# add index route

@bp.route('/')
def index():
    return "this is the pets index"

#now I need to register this route in the __init_py (factory) instance

