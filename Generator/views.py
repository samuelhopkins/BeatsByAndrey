import types, sys
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import json
import os
from django.http import HttpResponse, HttpResponseRedirect
from Generator.models import Artist
from Generator.FreestyleGenerator import Generator
from BackGround import backgroundThread
from django.core.files import File


def noClosures(lyrics):
	lyrics=lyrics
	for word in lyrics:
		if ('[' in word) or (']' in word):
			lyrics.remove(word)
		elif ('(' in word) or (')' in word):
			lyrics.remove(word)
	return lyrics

def index(request):
	objects=Artist.objects.order_by('created').reverse()
	available_list=[]
	for artist in objects:
		available_list.append(artist.name)

	return render_to_response('Generator/index.html',  {})

def available(request):
	objects=Artist.objects.order_by('created').reverse()
	available_list=[]
	for artist in objects:
		available_list.append(artist.name)

	return HttpResponse(json.dumps(",".join(available_list),ensure_ascii=False).encode('utf8'))

def undo(request):
	artist_name=request.GET['artist_name'].lower()
	print artist_name
	model=Artist.objects.get(name=artist_name)
	model.delete()
	return HttpResponse()

def create_thread(name):
	thread=backgroundThread(name)
	thread.start()
	return

def generated(request):
		model=0
		threads=[]
		context=RequestContext(request)
		strength=request.GET['strength']
		artist_name_upper=request.GET['artist_name']
		artist_name=artist_name_upper.lower()
		try:
			model=Artist.objects.get(name=artist_name)
		except Artist.DoesNotExist:
			create_thread(artist_name)
			print "not exist"
			return HttpResponse(json.dumps(unicode(artist_name),ensure_ascii=False).encode('utf8'))
		print model
		lyrics_list=list(json.loads(model.lyric_list))
		existing=Generator(lyrics_list)
		lyrics=existing.generate(250,int(strength))
		splitstyle=noClosures(lyrics.split())
		lyrics=(" ").join(splitstyle)
		lyrics.replace("\\","")
		lyrics=json.dumps(unicode(lyrics),ensure_ascii=False).encode('utf8')
		return HttpResponse(lyrics)



# Create your views here.
