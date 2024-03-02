from flask import Flask, render_template

app = Flask(__name__, static_folder="./frontend/static", template_folder="./frontend/templates")


@app.route('/')
def hello_world():
    return render_template('forum.html')


if __name__ == '__main__':
    app.run(debug=True)
