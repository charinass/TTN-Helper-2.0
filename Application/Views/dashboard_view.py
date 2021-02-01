from flask import render_template, redirect, url_for, session, request


from Application import app
from ..Controller.connect_mqtt import Connect


@app.route("/dashboard/", methods=["GET", "POST"])
def logged_in():
    username = request.args.get("user")
    passphrase = request.args.get("passphrase")
    broker = request.args.get("broker")
    topic = request.args.get("topic")

    if request.form.get("conn_btn"):
        conn = Connect(username, passphrase, broker, topic)
        conn.start_connecting()
        json_msg = conn.get_message()
        print(json_msg)

    return render_template("dashboard.html", page_title="Dashboard")


@app.route("/logout/")
def log_out():
    session.clear()
    return redirect(url_for("index", q="logout"))
