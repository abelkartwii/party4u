import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys

class Party():
    spotify_client_id = ""
    spotify_client_secret = ""
    spotify_redirect_url = "http://localhost:8080"

    sp = spotipy.Spotify(auth_manager = SpotifyOAuth())
    recents = sp.current_user_recently_played(limit = 50)
    if not len(recents):
        sys.exit("Sorry! Spotify can't process your recently played tracks.")