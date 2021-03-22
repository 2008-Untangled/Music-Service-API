from flask import Flask
from api import create_app
# from os import environ


# app = Flask(__name__)
# app.config.from_envvar('SPOTIFY_CLIENT_ID')
# app.config.from_envvar('SPOTIFY_CLIENT_SECRET')  

app = create_app()

if __name__ == '__main__':
  app.run()