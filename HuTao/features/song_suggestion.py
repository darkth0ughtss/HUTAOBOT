# BOT/features/song_suggestion.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from ..config import spotify_client_id, spotify_client_secret
import random

# Spotify API authentication
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret
))

