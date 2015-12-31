from sources import *
import sources

def search(query):
	for source in sources.sources:
		print eval(source).search(query)

search("Wilco")
