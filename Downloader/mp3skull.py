opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def getmp3s(url):
    response = opener.open(url)
    content = response.read()
    soup = BeautifulSoup(content)
    results = []
    for a in soup.findAll('a',href=re.compile('http.*\.mp3')):
        results.append(a['href'])
    return results

def skullid():
    response = opener.open("http://mp3skull.wtf/")
    content = response.read()
    soup = BeautifulSoup(content)
    return soup.find("input", {"name":"fckh"})["value"]

def search(query):
    return getmp3s("https://mp3skull.wtf/search_db.php?q="+query+"&fckh="+skullid())
