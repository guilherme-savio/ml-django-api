from django.apps import AppConfig
from GenrePredict.genre.auth import SpotifyAuth
from GenrePredict.settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


class GenreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'genre'
    spotify_auth = SpotifyAuth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    spotify_auth.authenticate()
