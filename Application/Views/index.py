from flask import render_template, request, url_for
from werkzeug.utils import redirect

from Application import app
from ..Controller.auth import Authentication
from .ttn_helper import logged_in


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        passphrase = request.form["ttn_passphrase"]
        a = Authentication()
        a.validate_user(username, passphrase)
        if a.rc_checker > 0 and a.rc_checker < 6:
            return render_template(
                "index.html", title="TTN Helper", response="Invalid user."
            )
        else:
            return redirect(url_for("logged_in", username=username))

    return render_template("index.html", title="TTN Helper")
