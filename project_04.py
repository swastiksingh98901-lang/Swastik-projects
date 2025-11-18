import random

# Create a playlist with at least 8 song titlesst
playlist = ['Chaiyya Chaiyya',"Kal Ho Naa Ho","Tujhe Dekha To","Raaataan Lambiyan","Badtameez Dil","Apna Bana Le","Lag Jaa Gale Se Phir","Agar Tum Saath Ho"]

print("Original Playlist:", playlist)

# Shuffle the playlist randomly
random.shuffle(playlist)
print("Shuffled Playlist:", playlist)

# Create a "Recently Played" list (last 3 songs) - assuming we simulate playing by slicing
recently_played = playlist[-3:]
print("Recently Played:", recently_played)

# Find duplicate songs and remove them (using set for uniqueness)
playlist = list(set(playlist))
print("Playlist after removing duplicates:", playlist)

# Create a backup copy of the original playlist (before modifications)
backup_playlist = playlist.copy()
print("Backup Playlist:", backup_playlist)

# Search for songs containing a specific word (e.g., "Love")
search_word = "Moods and Eras"
matching_songs = [song for song in playlist if search_word.lower() in song.lower()]
print(f"Songs containing '{search_word}': {matching_songs}")

# Merge two different playlists
another_playlist = [ "Tujhe Dekha To", "Raaataan Lambiyan", "Badtameez Dil"]
playlist.extend(another_playlist)
print("Merged Playlist:", playlist)

# Advanced Feature: Create a "Smart Playlist" that automatically adds songs based on criteria (e.g., all songs with "love" in the title)
smart_playlist = [song for song in playlist if "love" in song.lower()]
print("Smart Playlist (songs with 'love'):", smart_playlist)