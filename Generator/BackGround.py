import threading
import sys
import json
from Generator.models import Artist
from Generator.FreestyleGenerator import Generator, Scraper
from datetime import datetime
from django.core.files import File

class backgroundThread(threading.Thread):
	def __init__(self,name):
		super(backgroundThread,self).__init__()
		self.artist_name=name

	def run(self):
		print "in background thread"
		new_scraper=Scraper(unicode(self.artist_name).decode('utf8'))
		if len(new_scraper.songLyricList)>20:
			print len(new_scraper.songLyricList)
			new=Artist.objects.create(name=self.artist_name)
			new.lyric_list=json.dumps(new_scraper.songLyricList)
			new.created=datetime.now()
			# with open(self.artist_name,'w+') as f:
			# 	myfile=File(f)
			# 	json.dump(new_scraper.songLyricList,myfile)
			# 	new.lyrics_file.save(self.artist_name,myfile)
			# 	f.close()
			# 	myfile.close()
			new.save()
		else:
			print "too short"
			return
