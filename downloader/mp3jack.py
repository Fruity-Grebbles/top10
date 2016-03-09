from bs4 import BeautifulSoup
import re, urlparse
import string
import openurl, urllib
urllib._urlopener = openurl.opener()

def getmp3s(url):
    try:
        response = urllib.urlopen(url)
    except UnicodeEncodeError:
        response = urllib.urlopen(iriToUri(url))
        
    content = response.read()
    soup = BeautifulSoup(content,"lxml")
    results = []
    for a in soup.findAll('a',href=re.compile('http.*\.mp3')):
        results.append(a['href'])
    return results

def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)

def iriToUri(iri):
    parts= urlparse.urlparse(iri)
    return urlparse.urlunparse(
        part.encode('idna') if parti==1 else urlEncodeNonAscii(part.encode('utf-8'))
        for parti, part in enumerate(parts)
    )

def search(query):
	query= re.sub(r"\s+", '_', query)
    return getmp3s("http://www.mp3jack.in/?q="+query)
    
