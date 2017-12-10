# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify
import random
import datetime

# Define the blueprint: 'auth', set its url prefix: url/auth
mod_ui = Blueprint('ui', __name__, url_prefix='/')

# Set the route and accepted methods
@mod_ui.route('/', methods=['GET'])
def dashboard():
    return render_template("index.html")

mod_ui_api = Blueprint('ui_api', __name__, url_prefix='/api')

@mod_ui_api.route('/live_conditions', methods=['GET'])
def live_conditions():
    return jsonify({
        'temperature': {
            'value': random.randint(65,75),
            'unit': '&deg;F'
        },
        'humidity': {
            'value': random.randint(50,75),
            'unit': '%RH'
        },
        'water': {
            'value': random.randint(10,80),
            'unit': '%WV'
        },
        'date': datetime.date.today().strftime("%Y-%m-%d"),
        'time': datetime.datetime.now().strftime("%H:%M")
    })
