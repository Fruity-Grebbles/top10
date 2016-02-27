import mp3skull,pleer,emp3world
import openurl,urllib
import os

urllib._urlopener = openurl.opener()

def search(query):
    urls = []
    urls.extend(mp3skull.search(query))
    urls.extend(pleer.search(query))
    urls.extend(emp3world.search(query))
    return urls

def download(url,logfunc,outfile):
	f = open(outfile,"wb+")
	site = urllib.urlopen(url)
	meta = site.info()
	filesize = float(meta.getheaders("Content-Length")[0])
	logfunc(filesize)
	while True:
		block = site.read(4096) # read a 4k block from the file
		if len(block) == 0:
			break
		f.write(block)
		logfunc(str(os.stat(outfile).st_size/filesize*100))
	f.close()
