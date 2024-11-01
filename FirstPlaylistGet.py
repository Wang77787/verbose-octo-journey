from ytmusicapi import YTMusic

# Initialize YTMusic without authentication (public playlists don't require auth)
ytmusic = YTMusic()

# Replace this with your public playlist ID
playlist_id = "PLabc123..."  # Insert your playlist ID here

def get_playlist_songs(playlist_id):
    # Fetch playlist details
    playlist = ytmusic.get_playlist(playlist_id, limit=100)  # Increase limit if the playlist is larger

    # Open a file to write song titles and artist names
    with open("youtube_music_playlist_songs.txt", "w") as file:
        for song in playlist["tracks"]:
            title = song["title"]
            artist = ", ".join([artist["name"] for artist in song["artists"]])
            file.write(f"{title} - {artist}\n")
    print("Playlist data saved to youtube_music_playlist_songs.txt")

# Call the function
get_playlist_songs(playlist_id)
