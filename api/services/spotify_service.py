import json
import requests
import base64

# spotify_client_id = '0493107b40064a839fc4a359d9878cc8'
# spotify_client_sercret = '80d6738510ab495ca4b8cc880f47eb34'

class Spotify:
  def authorization_string(self, client_id, client_sercret):
    auth_str = '{}:{}'.format(client_id, client_sercret)
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
