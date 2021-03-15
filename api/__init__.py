from flask_restful import Api
from flask import Flask, jsonify
from config import config

def create_app(config_name='default'):
  app = Flask(__name__)
  app.config.from_object(config[config_name])

  @app.route('/', methods=['GET'])
  def home():
    return '''<h1>Welcome</h1>'''

  @app.errorhandler(404)
  def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

  
  return app