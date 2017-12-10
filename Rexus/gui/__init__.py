# Import flask and template operators
from flask import Flask, render_template

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from mod_data.controllers import mod_data as data_module
from mod_grow.controllers import mod_grow as grow_module
from mod_settings.controllers import mod_settings as settings_module
from mod_splash.controllers import mod_splash as splash_module

# Register blueprint(s)
app.register_blueprint(data_module)
app.register_blueprint(grow_module)
app.register_blueprint(settings_module)
app.register_blueprint(splash_module)
