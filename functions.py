from bs4 import BeautifulSoup
import urllib2
from urllib2 import urlopen, URLError, HTTPError
import spotipy
import re
import os

spotify = spotipy.Spotify()
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def dl(url,dldir):
    # Open the url
    try:
        f = urlopen(url)
        # Open our local file for writing
        with open(os.path.join(os.path.abspath(dldir), os.path.basename(url)), "wb") as local_file:
            local_file.write(f.read())

    #handle errors
    except Exception:
        raise

def getmp3s(url):
    response = opener.open(url)
    content = response.read()
    soup = BeautifulSoup(content)
    results = []
    for a in soup.findAll('a',href=re.compile('http.*\.mp3')):
        results.append(a['href'])
    return results

def getartist(artistname):
    results = spotify.search(q='artist:' + artistname, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        return artist

def skullid():
    response = opener.open("http://mp3skull.wtf/")
    content = response.read()
    soup = BeautifulSoup(content)
    return soup.find("input", {"name":"fckh"})["value"]

def searchskull(query):
    return getmp3s("https://mp3skull.wtf/search_db.php?q="+query+"&fckh="+skullid())

def toptracks(artistid):
    return spotify.artist_top_tracks(artistid)['tracks']

def top(logfunc,artistname,dldir):
    artist = getartist(str(artistname))
    logfunc("Downloading the top tracks of "+artist['name']+"\n")
    for track in toptracks(artist['uri'])[:10]: 
        logfunc("Downloading "+track['name']+"\n")
        for mp3 in searchskull(artist['name'].replace(" ", "+")+"+"+track['name'].replace(" ","+")):
            try:
                logfunc(mp3+"\n")
                dl(mp3,dldir)
                break
            except Exception:
                logfunc("Download failed. Trying another link...\n")
    logfunc("Done"+"\n")