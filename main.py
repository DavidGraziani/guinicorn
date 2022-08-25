from flask import Flask

def create_app(testing: bool = True):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return f"Hola mundo <br>Testing: {testing}"

    return app