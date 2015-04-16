import types, sys
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import json
from rq import Queue
from worker import conn
from django.http import HttpResponse, HttpResponseRedirect
from Generator.models import Artist
from Generator.FreestyleGenerator import Generator

q=Queue(connection=conn)

def noClosures(lyrics):
	lyrics=lyrics
	for word in lyrics:
		if ('[' in word) or (']' in word):
			lyrics.remove(word)
		elif ('(' in word) or (')' in word):
			lyrics.remove(word)
	return lyrics

def index(request):
	objects=Artist.objects.all()
	available_list=[]
	for artist in objects:
		if len(artist.lyric_list) > 50000:
			available_list.append(artist.name)

	return render_to_response('Generator/index.html',  {"available_list":available_list})

def undo(request):
	print "in undo"
	artist_name=request.GET['artist_name'].lower()
	print artist_name
	model=Artist.objects.get(name=artist_name)
	model.delete()
	new_Gen=Generator("")
	return HttpResponse()

def create_or_recieve(name):
	print "excepted"
	new=Artist.objects.create(name=name)
	new_Gen=Generator(artist_name)
	if new_Gen.songLyricList==[]:
		model.delete()
	else:
		model.lyric_list=json.dumps(new_Gen.songLyricList)
		model.save()

def generated(request):
		model=0
		context=RequestContext(request)
		strength=request.GET['strength']
		artist_name=request.GET['artist_name'].lower()
		try:
			model=Artist.objects.get(name=artist_name)
		except Artist.DoesNotExist:
			print "exceptional"
			result=q.enqueue(create_or_recieve,artist_name)
			exception=True
			return HttpResponse(json.dumps("nooooooooooooo"))
		
		lyrics_list=list(json.loads(model.lyric_list))
		existing=Generator(lyrics_list)
		lyrics=existing.generate(250,int(strength))

		splitstyle=noClosures(lyrics.split())
		lyrics=(" ").join(splitstyle)
		lyrics.replace("\\","")
		lyrics=json.dumps(unicode(lyrics),ensure_ascii=False).encode('utf8')
		return HttpResponse(lyrics)



# Create your views here.
