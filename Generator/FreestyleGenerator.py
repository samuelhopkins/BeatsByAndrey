# encoding: utf-8
import sys, types
from LyricScrape import LyricScraper
import random
import threading
from collections import defaultdict


#Neccessary to get rid of strings deliniating verses and chorus i.e. [Verse x2]
def noClosures(lyric):
	lyrics=lyric
	for string in lyrics:
		if (('[' in string) or
			 (']' in string) or
			 ('(' in string) or
			 (')' in string) or
			(':' in string)  or 
			('2' in string) ):
			lyrics.remove(string)
	return lyrics

class Generator():
	artist=""
	wordDict=defaultdict(set)
	wordList=[]
	songLyricList=[]
	def __init__(self, *args):
		if len(args)==1:
			arg=args[0]
		if hasattr(arg,'__iter__'):
			self.songLyricList=arg
		else:
			self.artist=arg
			scraped=LyricScraper(arg)
			lyrics=scraped.lyrics
			self.songLyricList=lyrics
			

	
			



	def train(self,strength):
		for song in self.songLyricList:
			songWordList=song.split()
			songWordList=noClosures(songWordList)
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
	new=Generator("Sam")


