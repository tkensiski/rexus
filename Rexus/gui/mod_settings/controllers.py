# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_settings = Blueprint('settings', __name__, url_prefix='/settings')

# Set the route and accepted methods
@mod_settings.route('/', methods=['GET'])
def dashboard():
    return render_template("settings/dashboard.html")
