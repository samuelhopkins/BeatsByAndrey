import types, sys
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import json
from django.http import HttpResponse, HttpResponseRedirect
from Generator.models import Artist
from Generator.FreestyleGenerator import Generator

def noClosures(lyrics):
	lyrics=lyrics
	for word in lyrics:
		if ('[' in word) or (']' in word):
			lyrics.remove(word)
		elif ('(' in word) or (')' in word):
			lyrics.remove(word)
	return lyrics

def index(request):
	return render_to_response('Generator/index.html',  {})

def undo(request):
	print "in undo"
	artist_name=request.GET['artist_name'].lower()
	print artist_name
	model=Artist.objects.get(name=artist_name)
	model.delete()
	new_Gen=Generator("")
	return HttpResponse()

def generated(request):
		model=0
		context=RequestContext(request)
		strength=request.GET['strength']
		artist_name=request.GET['artist_name'].lower()
		print artist_name
		model,created=Artist.objects.get_or_create(name=artist_name)
		if created:
			print "created"
			new_Gen=Generator(artist_name)
			if new_Gen.songLyricList==[]:
				model.delete()
				lyrics="Invalid artist name entered."
				return HttpResponse(json.dumps(lyrics))
			else:
				model.lyric_list=json.dumps(new_Gen.songLyricList)
				model.save()
		if len(model.lyric_list)< 50000:
			model.delete()
			lyrics="Insufficient Data."
			return HttpResponse(json.dumps(lyrics))
		if not created:
			print "existed"
			lyrics_list=list(json.loads(model.lyric_list))
			existing=Generator(lyrics_list)
			lyrics=existing.generate(250,int(strength))
		else:
			lyrics=new_Gen.generate(250,int(strength))

		splitstyle=noClosures(lyrics.split())
		lyrics=(" ").join(splitstyle)
		lyrics.replace("\\","")
		lyrics=json.dumps(unicode(lyrics),ensure_ascii=False).encode('utf8')
		return HttpResponse(lyrics)



# Create your views here.
