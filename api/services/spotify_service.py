import json
import requests
import base64
from os import environ

class Spotify:
  def authorization_string(self):
    auth_str = '{}:{}'.format(environ.get('SPOTIFY_CLIENT_ID'), environ.get('SPOTIFY_CLIENT_SECRET'))
    return base64.b64encode(auth_str.encode()).decode()
    
  def access_token(self, auth_string):
    auth_header = {
      "Authorization": f"Basic {auth_string}"
    }
    auth_body = {
      "grant_type": "client_credentials"
    }
    response = requests.post('https://accounts.spotify.com/api/token', data=auth_body, headers=auth_header)
    return response.json()['access_token']

  def track_search(self, access_token, song_query, limit):
    header = {
      "Authorization": f"Bearer {access_token}"
    }
    params = {
      "q": f"{song_query}",
      "type": "track",
      "market": "US",
      "limit": f"{limit}",
    }
    return requests.get('https://api.spotify.com/v1/search', params=params, headers=header)
