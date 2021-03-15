import json
import unittest

from api import create_app
from tests import assert_payload_field_type_value

class WelcomeTest(unittest.TestCase):
  def setUp(self):
    self.app = create_app('testing')
    self.app_context = self.app.app_context()
    self.app_context.push()
    self.client = self.app.test_client()

  def tearDown(self):
      self.app_context.pop()

  def test_welcome_page(self):
    response = self.client.get('/')
    self.assertEqual(200, response.status_code)
    self.assertEqual('<h1>Welcome</h1>', response.data.decode('utf-8'))

  def test_404_response(self):
    response = self.client.get('/2332sdfg345')
    self.assertEqual(404, response.status_code)
    self.assertEqual('<h1>404</h1><p>The resource could not be found.</p>', response.data.decode('utf-8'))