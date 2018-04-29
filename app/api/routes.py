from flask import jsonify
from app.api import api


@api.route('/')
def index():
    return jsonify({'hello': 'World'})
    