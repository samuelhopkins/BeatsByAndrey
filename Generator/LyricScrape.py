from bs4 import BeautifulSoup
import threading
import thread
import sys
import requests
import time
from urlparse import urljoin

listLock=threading.Lock()
#lyricList=[]
hrefBase="http://genius.com"

#Multithreaded web scraper thread function
class pageThread(threading.Thread):
	def __init__(self, threadID, URL, artist,lyricList):
		super(pageThread,self).__init__()
		self.artistString=artist
		self.threadID=threadID
		self.URL=URL
		self.lyricList=lyricList

	def run(self):
		artistUrl=self.URL
		response=requests.get(self.URL, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) \
			AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}) 
		soup=BeautifulSoup(response.text,'lxml')                  
		for song_link in soup.select('ul.song_list > li > a'):
			link = urljoin(hrefBase,song_link['href'])
			response = requests.get(link)
			soup = BeautifulSoup(response.text)
			title=soup.select('.text_artist > a')
			if unicode(title[0].text.lower().strip()).encode('utf8') == unicode(self.artistString).encode('utf8'):
				lyrics= soup.find('div', class_='lyrics').text.strip()
				listLock.acquire()
				self.lyricList.append(lyrics)
				listLock.release()
			else:
				continue

#Multithreaded web scraper to collect all lyrics for a musician from Genius.com
#Will access the first part of an artists songs and create threads 
#to scrape the lyric data from all subsequent pages
#Returns a list of all song lyrics to FreestyleGenerator.train()
class LyricScraper():
	def __init__(self,artist):
		self.BASE_URL="http://genius.com/search?q="
		self.BASE_QUERY="http://genius.com/search?page="
		self.artistString=artist
		artistList=artist.split()
		self.artist=("-").join(artistList)
		self.artist_URL=self.BASE_URL+"/"+self.artist+"/"
		self.lyrics=self.scrape()
		self.pages=0



	def scrape(self):
		self.threads=[]
		self.LList=[]
		tic=time.time()
		response=requests.get(self.artist_URL, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) \
			AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
		soup=BeautifulSoup(response.text,'lxml')  
		header=soup.select(".results_header")
		numSongs=header[0].text.split()[0]
		if numSongs.strip()=="Results":
			return []
		if int(numSongs) > 20000:
			return [] 
		#Genius.com lists 20 songs per page
		numPages=int(numSongs)/20
		self.pages=numPages
		for page in range(1,numPages):
			URL=self.BASE_QUERY+str(page)+"&q="+self.artist
			thread=pageThread(page,URL,self.artistString,self.LList)
			thread.start()
			self.threads.append(thread)
		#Wait for all threads to finish collecting lyrics
		before=0
		while threading.activeCount()>3:
			if threading.activeCount()!=before:
				print "active count is {0}".format(threading.activeCount())
				before=threading.activeCount()
		for t in self.threads:
			t.join()
		toc=time.time()
		print toc-tic,'s'
		return self.LList



