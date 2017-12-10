# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_grow = Blueprint('grow', __name__, url_prefix='/api/grow')

# Set the route and accepted methods
@mod_grow.route('/', methods=['GET'])
def dashboard():
    return jsonify({})
