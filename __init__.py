from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "MyGyno is live 🚀"

    return app
