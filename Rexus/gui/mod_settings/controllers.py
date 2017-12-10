# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify, current_app

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_settings = Blueprint('settings', __name__, url_prefix='/api/settings')

# Set the route and accepted methods
@mod_settings.route('/', methods=['GET'])
def dashboard():
    current_app.logger.info('testing')
    return jsonify({})
