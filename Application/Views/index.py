import logging
from flask import render_template, request, redirect, url_for, make_response

from Application import app, db
from ..Controller.auth import Authentication, User
from ..Models.TTN_User import TTN_User


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route("/", methods=["GET", "POST"])
def index(results=""):
    if request.method == "POST":
        username = request.form["username"]
        passphrase = request.form["ttn_passphrase"]  # not a password

        auth = Authentication()
        check_result = auth.check_if_user_exist(username, passphrase)  # returns a query

        if check_result is not None:
            resp = make_response(
                redirect(
                    url_for(
                        "logged_in",
                        user=check_result.username,
                        passphrase=check_result.password,
                        broker=check_result.broker,
                        topic=check_result.topic,
                    )
                )
            )
            resp.set_cookie("sessionID", "", expires=0)
            return resp
        else:
            results = {"response_msg": "No such user with that passphrase."}

    return render_template("index.html", results=results)


@app.route("/register/", methods=["GET", "POST"])
def register_user(results={"register": True}):
    if request.method == "POST":
        username = request.form["username"]
        passphrase = request.form["passphrase"]
        the_broker = request.form["the_broker"]
        the_topic = request.form["the_topic"]

        user = User()
        user.check_if_user_valid(username, passphrase, the_broker, the_topic)
        if not getattr(user, "rc_checker") == 0:
            results = {
                "register": True,
                "response_msg": "User is not registered to TTN",
            }

        elif getattr(user, "rc_checker") == 0:
            auth = Authentication()
            if auth.check_if_user_exist(username, passphrase) is not None:
                results = {
                    "register": True,
                    "response_msg": "User already exist in this WebApp.",
                }
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
            results = {
                "register": True,
                "response_msg": "There was an error with your request.",
            }

    return render_template(
        "index.html", page_title="Register to WebApp", results=results
    )
