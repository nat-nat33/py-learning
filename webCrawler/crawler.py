#Single Threaded Web Crawler
"""Basic Python Web Crawler"""

from collections import deque
import urllib.request
from bs4 import BeautifulSoup

def crawler():
	"""py web crawler"""
	url_queue = deque([
		'http://www.justjared.com/' 
		])
	
	visited = set()

	while len(url_queue):
		url = url_queue.popleft()
		visited.add(url)
		html = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(html, 'html.parser')
		
		for link in soup.find_all('a'):
			print(link.get('href'));

crawler();
