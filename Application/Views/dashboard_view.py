from flask import render_template, abort, redirect, url_for, session, request

from Application import app
from ..Controller import connect_mqtt


@app.route("/dashboard/")
def logged_in():
    return render_template("dashboard.html", title="Dashboard")


@app.route("/logout/")
def log_out():
    session.clear()
    return redirect(url_for("index", q="logout"))
