from django.db import models
from datetime import datetime

class Artist(models.Model):
	name=models.CharField("Artist's Name",primary_key=True,max_length=30)
	lyric_list=models.TextField()
	created=models.DateTimeField(default=datetime.now())

	def __unicode__(self):
		return self.name

	
# Create your models here.
