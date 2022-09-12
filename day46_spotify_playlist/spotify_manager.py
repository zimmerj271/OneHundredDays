import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# get Spotify client ID and secret from https://developer.spotify.com
SPOTIFY_CLIENT_ID = os.environ("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ("SPOTIFY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "https://www.example.com"


class Spotify:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                       client_secret=SPOTIFY_CLIENT_SECRET,
                                                       redirect_uri=SPOTIPY_REDIRECT_URI,
                                                       scope="playlist-modify-private",
                                                       cache_path="token.txt"))
        self.user_id = self.getUserID()

    def getUserID(self):
        user = self.sp.current_user()
        return user["id"]

    def getUserName(self):
        return self.sp.current_user()['display_name']

    def createPlaylist(self, name, description=None):
        playlist = self.sp.user_playlist_create(user=self.user_id,
                                     name=name,
                                     public=False,
                                     collaborative=False,
                                     description=description)
        return playlist["id"]

    def getTrackID(self, track, artist):
        query = self.sp.search(q="artist:" + artist + " track:" + track, limit=1)
        if len(query["tracks"]["items"]) == 0:
            return None
        return query["tracks"]["items"][0]["uri"]

    def addSongToPlaylist(self, playlist_id, track_list):
        self.sp.playlist_add_items(playlist_id=playlist_id, items=track_list)

