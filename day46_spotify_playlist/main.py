from billboard import Billboard
from spotify_manager import Spotify

playlist_date = input("Which year do you want to travel to (YYYY-MM-DD)? ")  # Get date for song list
billboard_songs = Billboard(playlist_date).song_list  # top 100 songs from Billboard for the date given
song_list = list(billboard_songs)  # zipped object converted to list of tuples
spotify_manager = Spotify()
playlist_name = f"Billboard Top 100 {playlist_date}"
playlist_description = f"Top 100 songs on the Billboard charts for the {playlist_date}"
playlist = spotify_manager.createPlaylist(name=playlist_name, description=playlist_description)  # create the playlist on Spotify

# Get track IDs for each song on the list
track_ids = []
for song in song_list:
    track = song[0]
    artist = song[1]
    track_id = spotify_manager.getTrackID(track, artist)
    if track_id is not None:
        track_ids.append(track_id)

spotify_manager.addSongToPlaylist(playlist_id=playlist, track_list=track_ids)  # Add the tracks to the playlist
