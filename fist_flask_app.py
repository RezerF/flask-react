from flask import Flask

app = Flask(__name__)

"""https://python-scripts.com/flask-react-from-zero"""

@app.route('/')
def hello_world():
    return 'Привет от Flask!'


if __name__ == "__main__":
    app.run()
