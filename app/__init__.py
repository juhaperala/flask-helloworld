import logging
from flask import Flask

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)

    from app.api import api
    app.register_blueprint(api)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)
    
    return app
