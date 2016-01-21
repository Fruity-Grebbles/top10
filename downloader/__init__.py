import mp3skull,pleer,emp3world
import urllib2

def search(query):
    urls = []
    urls.extend(mp3skull.search(query))
    urls.extend(pleer.search(query))
    urls.extend(emp3world.search(query))
    return urls
    
def download(url,logfunc,file_name):
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        percent = file_size_dl * 100. / file_size
        logfunc(percent)
    logfunc(0)
    f.close()
