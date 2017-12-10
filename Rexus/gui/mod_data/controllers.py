# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_data = Blueprint('data', __name__, url_prefix='/data')

# Set the route and accepted methods
@mod_data.route('/', methods=['GET'])
def dashboard():
    return render_template("data/dashboard.html")
