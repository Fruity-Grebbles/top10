from sources import *
import sources
import urllib2

def search(query):
    urls = []
    for source in sources.sources:
        urls.extend(eval(source).search(query))
    return urls
    
def download(url,logfunc):
    file_name = url.split('/')[-1]
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
    f.close()
