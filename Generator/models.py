from django.db import models


class Artist(models.Model):
	name=models.CharField("Artist's Name",primary_key=True,max_length=30)
	lyric_list=models.TextField()

	def __unicode__(self):
		return self.name

# Create your models here.
