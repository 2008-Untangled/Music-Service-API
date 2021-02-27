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