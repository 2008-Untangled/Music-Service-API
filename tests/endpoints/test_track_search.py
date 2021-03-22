import json
import unittest

from api import create_app
from api.resources.track_search import Track 
from http import client

class TrackSearchTest(unittest.TestCase):
  def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

  def tearDown(self):
      self.app_context.pop()
        
  def test_track_search(self):
      query = 'Yesterday'
      response = self.client.get(
      f'/api/v1/track?{query}'
      )
      self.assertEqual(200, response.status_code)

      data = json.loads(response.data.decode('utf-8'))
      
      results = data['data']

      self.assertEqual('Yesterday - Remastered 2009', results['song'])
      self.assertEqual('https://open.spotify.com/track/3BQHpFgAp4l80e1XslIjNI', results['url'])
      self.assertEqual('The Beatles', results['artist_name'])
      self.assertEqual('Help! (Remastered)', results['album_name'])
      self.assertEqual('1965-08-06', results['album_release_date'])

  def test_sad_path_track_search(self):
      query = ''
      response = self.client.get(
      f'/api/v1/track?{query}'
      )
      self.assertEqual(422, response.status_code)

      data = json.loads(response.data.decode('utf-8'))

      self.assertEqual(422, data['error'])
      self.assertEqual('Unprocessable Entity, please try another song title', data['message'])
    