from __future__ import division
from django.db import models
from datetime import datetime
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='static/Generator/lyrics')



class Artist(models.Model):
	name=models.CharField("Artist's Name",primary_key=True,max_length=30)
	lyric_list=models.TextField()
	created=models.DateTimeField(default=datetime.now())
	#lyrics_file=models.FileField(upload_to='artists')

	def __unicode__(self):
		return self.name

	
# Create your models here.
