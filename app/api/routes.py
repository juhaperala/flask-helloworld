from flask import jsonify, current_app
from app.api import api


@api.route('/')
def index():
    current_app.logger.info('hello')
    return jsonify({'hello': 'World'})
