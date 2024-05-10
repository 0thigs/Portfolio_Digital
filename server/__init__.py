from flask import Flask

dir_template_folder = '../src/templates/'
dir_static_folder = "../src/static"

def Create_app():
    app = Flask(__name__, template_folder=dir_template_folder, static_folder=dir_static_folder)
    return app

app = Create_app()

from server.routes import routes