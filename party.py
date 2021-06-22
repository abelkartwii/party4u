import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
import psycopg2

class Party():
    spotify_client_id = ""
    spotify_client_secret = ""
    spotify_redirect_url = "http://localhost:8080"

    sp = spotipy.Spotify(auth_manager = SpotifyOAuth())
    recents = sp.current_user_recently_played(limit = 50)
    if not len(recents):
        sys.exit("Sorry! Spotify can't process your recently played tracks. Try again?")

    album_list = []
    for row in recently_played['items']:
        album_id = row['track']['album']['id']
        album_name = row['track']['album']['name']
        album_release_date = row['track']['album']['release_date']
        album_total_tracks = row['track']['album']['total_tracks']
        album_url = row['track']['album']['external_urls']['spotify']
        album_element = {'album_id':album_id,'name':album_name,'release_date':album_release_date,
                        'total_tracks':album_total_tracks,'url':album_url}
        album_list.append(album_element)

    artist_dict = {}

    conn.commit()
    return "ETL from Spotify completed!"