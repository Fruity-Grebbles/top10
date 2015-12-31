from sources import *
import sources

def search(query):
	for source in sources.sources:
		urls.extend(eval(source).search(query))
    return urls
    
