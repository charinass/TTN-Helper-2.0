from flask import render_template, abort, redirect, url_for, session, request

from Application import app
from ..Models.TTN_User import TTN_User


@app.route("/dashboard/<string:username>")
def logged_in(username):
    if TTN_User.query.filter_by(username=TTN_User.username).scalar() is not None:
        return render_template("dashboard.html", title="Dashboard")
    else:
        abort(404)


@app.route("/logout/")
def log_out():
    session.clear()
    return redirect(url_for("index", q="logout"))
