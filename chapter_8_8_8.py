# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album(artist,title):
     album = (artist,title)
     return album
while True:
    print("\n'Tell me the name of an album's artist and the album's name.")
    print("(enter q to quit)")
    
    artist = input('artist: ')
    if artist == 'q':
        break
    
    title = input('title: ')
    if title == 'q':
        break
    
    print(make_album(artist,title))