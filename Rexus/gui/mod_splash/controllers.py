# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for


# Define the blueprint: 'auth', set its url prefix: url/auth
mod_splash = Blueprint('splash', __name__, url_prefix='/')

# Set the route and accepted methods
@mod_splash.route('/', methods=['GET'])
def dashboard():
    return render_template("splash/index.html")
