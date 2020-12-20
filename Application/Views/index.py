import logging
from flask import render_template, request, redirect, url_for, make_response

from Application import app, db
from ..Controller.auth import Authentication, User
from ..Models.TTN_User import TTN_User


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        passphrase = request.form["ttn_passphrase"]  # not a password
        if Authentication.check_if_user_exist(username, passphrase) == True:
            resp = make_response(render_template("dashboard.html", username=username))
            resp.set_cookie("sessionID", username, expires=0)
            return resp
        else:
            return render_template(
                "index.html",
                title="TTN Helper",
                response="No such user with that passphrase.",
            )
    return render_template("index.html", title="TTN Helper")


@app.route("/register/", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        username = request.form["username"]
        passphrase = request.form["passphrase"]
        the_broker = request.form["the_broker"]
        the_topic = request.form["the_topic"]
        user = User()
        user.check_if_user_valid(username, passphrase, the_broker, the_topic)
        if not getattr(user, "rc_checker") == 0:
            return render_template(
                "index.html",
                title="Register User",
                register=True,
                response="User is not registered to TTN.",
            )
        elif getattr(user, "rc_checker") == 0:
            if Authentication.check_if_user_exist(username, passphrase) == True:
                return render_template(
                    "index.html",
                    title="Register User",
                    register=True,
                    response="User already exist.",
                )
            else:
                query_add_user = TTN_User(
                    username=username,
                    password=passphrase,
                    broker=the_broker,
                    topic=the_topic,
                )
                try:
                    db.session.add(query_add_user)
                    db.session.commit()
                    return redirect(url_for("index", register="successful"))
                except:
                    logging.error("Error adding user.")

        else:
            return render_template(
                "index.html",
                title="Register User",
                register=True,
                response="There was an error with your request.",
            )

    return render_template("index.html", title="Register User", register=True)
