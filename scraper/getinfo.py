import spotipy
spotify = spotipy.client

def getartist(artistname):
    results = spotify.search(q='artist:' + artistname, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        return artist
        
def toptracks(artistid):
    return spotify.artist_top_tracks(artistid)['tracks']
