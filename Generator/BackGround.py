import threading
import sys
import json
from Generator.models import Artist
from Generator.FreestyleGenerator import Generator
from datetime import datetime

class backgroundThread(threading.Thread):
	def __init__(self,name):
		super(backgroundThread,self).__init__()
		self.artist_name=name

	def run(self):
		print "in background thread"
		new_Gen=Generator(self.artist_name)
		if len(new_Gen.songLyricList)>20:
			print len(new_Gen.songLyricList)
			print "creating"
			new=Artist.objects.create(name=self.artist_name)
			new.lyric_list=json.dumps(new_Gen.songLyricList)
			new.created=datetime.now()
			print "saving model"
			new.save()
		else:
			return
