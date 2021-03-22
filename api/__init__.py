from flask_restful import Api
from flask import Flask, jsonify, request
from config import config
from api.resources.track_search import Track 

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
    search = Track()
    if not query_params:
      return jsonify({
        'error': 422,
        'message': 'Unprocessable Entity, please try another song title'
      }), 422
    else:
      track_data = search.track_search(list(query_params.keys())[0])
      return jsonify(track_data['data']), track_data['status']
  
  return app