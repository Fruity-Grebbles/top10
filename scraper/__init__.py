import pylast
API_KEY = '71e7585c4ca3cb8c0e160246bfee4385'
API_SECRET = 'a90f951842bad467949b613490ccbe6f'

network = pylast.LastFMNetwork(API_KEY, api_secret = API_SECRET)

def getartist(artistname):
    return network.get_artist(artistname)
        
def toptracks(artist):
    return artist.get_top_tracks()
