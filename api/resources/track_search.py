import json
import requests
from api.services.spotify_service import Spotify

class Track:
  def track_search(self):
    service = Spotify()
    token = service.access_token(service.authorization_string())
    song_query = 'Yesterday'
    limit = 1

    response = service.track_search(token, song_query, limit)
    response_data = json.loads(response.text)
    return response_data