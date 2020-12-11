from flask import render_template

from Application import app


@app.route("/")
def index():
    return render_template("index.html", title="TTN Helper")
