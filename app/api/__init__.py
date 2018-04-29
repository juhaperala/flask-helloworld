from flask import Blueprint

api = Blueprint('main', __name__)

from app.api import routes
