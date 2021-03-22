import json
import requests
from api.services.spotify_service import Spotify

class Track:
  def track_search(self, query):
    service = Spotify()
    token = service.access_token(service.authorization_string())
    song_query = query
    limit = 1

    response = service.track_search(token, song_query, limit)
    response_data = json.loads(response.text)
    if not response_data['tracks']['total']:
      data = {
        'status': 422,
        'message': 'Unprocessable Entity, please try another song title'
        }
      return {
        'data': data,
        'status': 422
      }
    else:
      response_data_song = response_data['tracks']['items'][0]
      song_name = response_data['tracks']['items'][0]['name']
      song_url = response_data['tracks']['items'][0]['external_urls']['spotify']
      artist_name = response_data['tracks']['items'][0]['artists'][0]['name']
      album_name = response_data['tracks']['items'][0]['album']['name']
      album_release_date = response_data['tracks']['items'][0]['album']['release_date']

      song_data = {
        'data': {
          'song': song_name,
          'url': song_url,
          'artist_name': artist_name,
          'album_name': album_name,
          'album_release_date': album_release_date
        }
      }
      return {
        'data': song_data,
        'status': 200
      }