import json
import unittest
from api.resources.track_search import Track 

class TrackSearchTest(unittest.Testcase):
  def test_track_search(self):
      query = 'Yesterday'
      response = self.client.get(
      f'/api/v1/track?{query}'
      )
      self.assertEqual(200, response.status_code)

      data = json.loads(response.data.decode('utf-8'))
      assert_payload_field_type_value(self, data, 'success', bool, True)
      
      results = data['data']
     
      assert_payload_field_type_value(
            self, results, 'song_name', str, 'Yesterday - Remastered 2009'
        )
      assert_payload_field_type_value(
          self, results, 'song_url', str, 'https://open.spotify.com/track/3BQHpFgAp4l80e1XslIjNI'
      )
      assert_payload_field_type_value(
          self, results, 'artist_name', int, 'The Beatles'
      )
      assert_payload_field_type_value(
          self, results, 'album_name', int, 'Help! (Remastered)'
      )
      assert_payload_field_type_value(
          self, results, 'album_release_date', int, '1965-08-06'
      )