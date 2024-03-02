from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")
def home_page():
    return render_template("login.html")

@views.route("/login")
def login_page():
    return render_template("login.html")
