import mp3skull,pleer,emp3world
import os
import openurl

opener = openurl.opener()
def search(query):
    urls = []
    urls.extend(mp3skull.search(query))
    urls.extend(pleer.search(query))
    urls.extend(emp3world.search(query))
    return urls
    
def download(url,logfunc,file_name):
    u = opener.open(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    file_size_dl = 0
    block_sz = 8192
    try:
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            percent = file_size_dl * 100. / file_size
            logfunc(percent)
        f.close()
    except Exception:
        os.remove(f)
        raise
    logfunc(0)
