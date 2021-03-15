import json
import unittest

from api import create_app

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