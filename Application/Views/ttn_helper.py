from flask.templating import render_template
from flask import render_template
from Application import app


@app.route("/ttn-helper/<username>")
def logged_in(username):
    return render_template("ttn-helper.html")
