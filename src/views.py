from src.app import app, db
from src.oauth import vk
from src.models import Friend, User
from flask_login import current_user, login_user, logout_user
from flask import redirect, url_for, render_template, request, jsonify
import json


@app.route("/")
def index():
    if current_user.is_anonymous:
        return redirect(url_for("login"))
    return render_template("index.html", user=current_user, friends=current_user.friends)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/authorize/vk")
def oauth_authorize():
    if not current_user.is_anonymous:
        return redirect(url_for("index"))

    return redirect(vk.get_authorize_url(
            scope="friends",
            response_type="code",
            display="popup",
            redirect_uri="http://127.0.0.1:5000{}".format(url_for("oauth_callback"))
        ))


@app.route("/callback/vk")
def oauth_callback():
    if not current_user.is_anonymous:
        return redirect(url_for("index"))

    if "code" not in request.args:
        return jsonify({"Error": "requst has no <code> param"})

    oauth_session = vk.get_auth_session(
        data={
            "code": request.args["code"],
            "grant_type": "authorization_code",
            "redirect_uri": "http://127.0.0.1:5000{}".format(url_for("oauth_callback"))
        },
        decoder = json.loads
    )
    me = oauth_session.get("users.get?access_token={}&v={}".format(oauth_session.access_token,
                                                                   "5.103")).json()["response"][0]
    user = User.query.get(int(me["id"]))
    if user is not None:
        login_user(user)
    else:
        user = User(id=me["id"], username="{} {}".format(me["first_name"], me["last_name"]))
        db.session.add(user)
        db.session.commit()
        login_user(user)
        friends = oauth_session.get("friends.get?access_token={}&v={}".format(oauth_session.access_token,
                                                                              "5.103")).json()['response']['items'][0:5]
        ids = "{},{},{},{},{}".format(friends[0], friends[1], friends[2], friends[3], friends[4])
        friends = oauth_session.get("users.get?access_token={}&v={}&user_ids={}".format(oauth_session.access_token,
                                                        "5.103", ids)).json()["response"]
        for friend in friends:
            f = Friend(id = friend["id"], username="{} {}".format(friend["first_name"], friend["last_name"]),
                       is_friends=user)
            db.session.add(f)
            db.session.commit()

    return redirect(url_for("index"))


