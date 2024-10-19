from flask import Flask, render_template
from app import views


app = Flask(__name__, static_folder="./frontend/static", template_folder="./frontend/templates")

app.register_blueprint(views.views, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=False)
