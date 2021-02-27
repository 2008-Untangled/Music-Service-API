import json
import unittest
from api.services.spotify_service import Spotify


class SpotifyServiceTest(unittest.TestCase):
    def test_64_bit_conversion(self):
      client_id = '0493107b40064a839fc4a359d9878cc8'
      client_sercret = '80d6738510ab495ca4b8cc880f47eb34'
      service = Spotify()

      expected = service.authorization_string(client_id, client_sercret)

      assert expected == 'MDQ5MzEwN2I0MDA2NGE4MzlmYzRhMzU5ZDk4NzhjYzg6ODBkNjczODUxMGFiNDk1Y2E0YjhjYzg4MGY0N2ViMzQ='

    def test_get_access_token(self):
      authorization_string = 'MDQ5MzEwN2I0MDA2NGE4MzlmYzRhMzU5ZDk4NzhjYzg6ODBkNjczODUxMGFiNDk1Y2E0YjhjYzg4MGY0N2ViMzQ='
      service = Spotify()

      expected = service.access_token(authorization_string)

      self.assertIsInstance(expected, str)

    def test_return_track_search(self):
      client_id = '0493107b40064a839fc4a359d9878cc8'
      client_sercret = '80d6738510ab495ca4b8cc880f47eb34'
      service = Spotify()

      auth_string = service.authorization_string(client_id, client_sercret)
      token = service.access_token(auth_string)
      song_query = 'Yesterday'
      limit = 1

      response = service.track_search(token, song_query, limit)
      response_data = json.loads(response.text)

      self.assertEqual(200, response.status_code)

      response_data_song = response_data['tracks']['items'][0]
      song_name = response_data['tracks']['items'][0]['name']
      song_url = response_data['tracks']['items'][0]['external_urls']['spotify']
      artist_name = response_data['tracks']['items'][0]['artists'][0]['name']
      album_name = response_data['tracks']['items'][0]['album']['name']
      album_release_date = response_data['tracks']['items'][0]['album']['release_date']

      assert song_name == 'Yesterday - Remastered 2009'
      assert song_url == 'https://open.spotify.com/track/3BQHpFgAp4l80e1XslIjNI'
      assert artist_name == 'The Beatles'
      assert album_name == 'Help! (Remastered)'
      assert album_release_date == '1965-08-06'

