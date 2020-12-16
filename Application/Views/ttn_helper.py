from flask import render_template, abort

from Application import app
from ..Models.TTN_User import TTN_User


@app.route("/ttn-helper/<string:username>")
def logged_in(username):
    if TTN_User.query.filter_by(username=TTN_User.username).scalar() is not None:
        return render_template("ttn-helper.html")
    else:
        abort(404)
