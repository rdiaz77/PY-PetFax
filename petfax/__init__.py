#environment configuration

# python3 -m venv venv                
# . venv/bin/activate   
#then
# pip install Flask                  

# initial configuration to use Flask
# index route
# As we just learned, to create a route we need to call .route() on the app instance.
# The method expects at least one argument specifying what endpoint to use for the route. Let's just have it go to '/'
# To tell our route what to do when that endpoint is used, we need to define a method directly underneath it. Let's name our method index

# create global application factory instance
# the folder containing the app factory has to be created at the same level of the file that will be using the instance
from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def hello():
        return "hello, PetFax"
# importing and registering the pet.py/index route
# importing the blueprint (the name is the first argument in the bp instance)
    from . import pet 
    
# registering the blueprint as part of the app instance of flask in create_app()
    app.register_blueprint(pet.bp)
    

    return app
    