# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

def make_album(artist_name, album_title, tracks_num=0):
    if tracks_num:
        d = {
            "artist_name": artist_name,
            "album_title": album_title,
            "tracks number": str(tracks_num)
        }
    else:
        d = {
            "artist_name": artist_name,
            "album_title": album_title
        }
    
    return d

dict1 = make_album("The beatles","White album")
print(dict1)

dict2 = make_album("Linkin Park","Meteora")
print(dict2)

dict3 = make_album("Slip Knot","Iowa")
print(dict3)

# Add an optional parameter to make_album() that allows you to store the number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new function call that includes the number of tracks on an album.

dict4 = make_album("Metallica", "Black album", 12)
print(dict4)