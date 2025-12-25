from flask import Flask
from .config import Config
from .routes import main
from .db import db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here-make-it-long-and-random'
    app.config.from_object(Config)
    
    db.init_app(app)

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()


    return app