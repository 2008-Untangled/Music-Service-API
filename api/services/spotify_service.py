import json
import requests
import base64

client_id = '0493107b40064a839fc4a359d9878cc8'
client_sercret = '80d6738510ab495ca4b8cc880f47eb34'

auth_str = '{}:{}'.format(client_id, client_sercret)
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

auth_header = {
  "Authorization": f"Basic {b64_auth_str}"
}

auth_body = {
  # "Content-Type": "application/x-www-form-urlencoded",
  "grant_type": "client_credentials"
}

response = requests.post('https://accounts.spotify.com/api/token', data=auth_body, headers=auth_header)

access_token = response.json()['access_token']

header = {
  "Authorization": f"Bearer {access_token}"
}

track_query = 'Yesterday'

params = {
  "q": f"{track_query}",
  "type": "track",
  "market": "US",
  "limit": 5,
}

response = requests.get('https://api.spotify.com/v1/search', params=params, headers=header)

response_data = json.loads(response.text)

response_data_first_song = response_data['tracks']['items'][0]
first_song_name = response_data['tracks']['items'][0]['name']
song_url = response_data['tracks']['items'][0]['external_urls']['spotify']
artist_name = response_data['tracks']['items'][0]['artists'][0]['name']
album_name = response_data['tracks']['items'][0]['album']['name']
album_release_date = response_data['tracks']['items'][0]['album']['release_date']