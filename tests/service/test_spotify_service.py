import json
import unittest
from api.services.spotify_service import Spotify


class SpotifyServiceTest(unittest.TestCase):
    def test_64_bit_conversion(self):
      service = Spotify()
      expected = service.authorization_string()
      self.assertIsInstance(expected, str)

    def test_get_access_token(self):
      service = Spotify()
      expected = service.access_token(service.authorization_string())
      self.assertIsInstance(expected, str)

    def test_return_track_search(self):
      service = Spotify()
      token = service.access_token(service.authorization_string())
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

    def test_return_track_search(self):
      service = Spotify()
      token = service.access_token(service.authorization_string())
      song_query = ''
      limit = 1

      response = service.track_search(token, song_query, limit)
      response_data = json.loads(response.text)
      info = response_data['error']

      self.assertEqual(400, response.status_code)
      self.assertEqual(400, info['status'])
      self.assertEqual('No search query', info['message'])

