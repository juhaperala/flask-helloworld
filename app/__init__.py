import logging
from flask import Flask

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.api import api
    app.register_blueprint(api)

    fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fmt)
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)
    
    return app
