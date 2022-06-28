# Remember, creating a new blueprint instance requires three arguments:
# The name of the blueprint. Let's name ours pet.
# The location of the blueprint. We can just use the handy __name__.
# The URL prefix that should be used for all routes attached to this blueprint. Let's go with /pets.


from flask import Blueprint

bp = Blueprint ("pet", __name__, url_prefix="/pets" ) 