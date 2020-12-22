from flask import render_template, redirect, url_for, session, make_response


from Application import app
from ..Controller.connect_mqtt import Connect


@app.route("/dashboard/")
def logged_in(check_result):

    return make_response(render_template())


def connect_to_device():

    return "connected"


@app.route("/logout/")
def log_out():
    session.clear()
    return redirect(url_for("index", q="logout"))
