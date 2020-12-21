from flask import render_template, redirect, url_for, session, make_response

from Application import app
from ..Controller import connect_mqtt


@app.route("/<username>/")
def logged_in(username):
    resp = make_response(render_template("dashboard.html", username=username))
    resp.set_cookie("sessionID", username, expires=0)
    return resp


@app.route("/logout/")
def log_out():
    session.clear()
    return redirect(url_for("index", q="logout"))
