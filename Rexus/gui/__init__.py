# Import flask and template operators
from flask import Flask, render_template, logging
import logging
from logging.handlers import RotatingFileHandler

# Define the WSGI application object
app = Flask(__name__)

file_handler = RotatingFileHandler(
    'logs/gui.log',
    maxBytes=1000 * 1000 * 100,
    backupCount=2
)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(asctime)s][%(levelname)s][%(name)s.%(module)s:%(lineno)d] %(message)s")
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)

for llogger in app.logger.handlers:
    llogger.setFormatter(formatter)

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
from mod_ui.controllers import (
    mod_ui as ui_module,
    mod_ui_api as ui_api_module
)

# Register blueprint(s)
app.register_blueprint(data_module)
app.register_blueprint(grow_module)
app.register_blueprint(settings_module)
app.register_blueprint(ui_module)
app.register_blueprint(ui_api_module)

app.logger.info('Rexus GUI Loaded')
