# encoding: utf-8
import sys, types
from LyricScrape import LyricScraper
import random
import threading
from collections import defaultdict
import re

			
class Scraper():
	def __init__(self,artist_name):
		self.artist=artist_name
		scraped=LyricScraper(self.artist)
		lyrics=scraped.lyrics
		self.songLyricList=lyrics

class Generator():
	def __init__(self, lyrics_list):
		self.songLyricList=lyrics_list
		self.wordDict=defaultdict(set)
		self.wordList=[]
			



	def train(self,strength):
		for song in self.songLyricList:
			song = re.sub(r'[^a-zA-Z\.,\' ]+', ' ', song)
			songWordList = song.split()
			length=len(songWordList)
			for i in range(length-strength):
				keyTup=()
				step=0
				j=i
				while (step<strength):
					keyTup+=(songWordList[j],)
					step+=1
					j+=1
				self.wordDict[keyTup].add(songWordList[j])
		self.wordList=self.wordDict.keys()

#generate will generate a freestyle of "length" many words
	def generate(self,length,strength):
		self.train(strength)
		print "trained"
		options=len(self.wordList)
		rand=random.randint(0,options)
		seed=self.wordList[rand]
		freeStyle=u""
		for i in range(length):
			follows=list(self.wordDict[seed])
			followsLen=len(follows)
			if followsLen is 0:
				seed=self.wordList[random.randint(0,options-1)]
				i-=1
				continue
			nextTup=()
			nextTup+=seed[1:]
			randNextInt=random.randint(0,followsLen-1)
			next=follows[randNextInt]
			freeStyle+=" "+unicode(next)
			nextTup+=(next,)
			seed=nextTup
		return freeStyle



if __name__=="__main__":
	new=Generator("")


