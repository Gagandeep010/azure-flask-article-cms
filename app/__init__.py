from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
