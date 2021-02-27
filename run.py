from flask import Flask
# from os import environ


app = Flask(__name__)
# app.config.from_envvar('SPOTIFY_CLIENT_ID')
# app.config.from_envvar('SPOTIFY_CLIENT_SECRET')  

if __name__ == '__main__':
  app.run()