from flask import Flask


app = Flask('Rexus')

@app.route("/")
def hello():
    return "Rexus!"
