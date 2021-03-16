from flask_restful import Api
from flask import Flask, jsonify, request
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

  @app.route('/api/v1/track', methods=['GET'])
  def api_filter():
    query_params = request.args
    track_query = query_params.get('track')
    return jsonify(query_params)
  
  return app