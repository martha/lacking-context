import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

def get_album_details(album_id):
  try:
    client_id = os.environ['SPOTIFY_CLIENT_ID']
    client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
  except(KeyError):
    print('Oop, it looks like you haven\'t yet set your SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET environment variables.')
    return None

  client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret)
  spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

  try:
    results = spotify.album('spotify:album:%s' % album_id)
    listen_url = results['external_urls']['spotify']
    image_url = results['images'][0]['url']
    return {
      'listen_url': listen_url,
      'image_url': image_url
    }
  except(spotipy.client.SpotifyException):
    print('Oh no! \'%s\' is not a valid album id' % album_id)
    return None
