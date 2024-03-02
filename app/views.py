from flask import Blueprint, render_template, request
from app.db import db

views = Blueprint('views', __name__)


@views.route("/")
def home_page():
    return render_template("login.html")


@views.route("/login")
def login_page():
    return render_template("login.html")


@views.route("/new-post", methods=["GET", "POST"])
def new_post():
    if request.method == 'GET':
        pass

    else:
        try:
            last_post_id = db["posts"].find(sort=[('_id', -1)])  # returns last post from sorted list
            last_post_id = last_post_id[0]['_id']  # _id of last post
        except:
            last_post_id = 0

        post_id = last_post_id + 1

        post_type = request.form.get("post_type")
