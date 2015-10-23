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
import re



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
	artist_names=request.GET['artist_names']
	artist_names=set(artist_names.split(','))
	for name in artist_names:
		print name
		name=name.lower()
		model=Artist.objects.get(name=name)
		model.delete()
	return HttpResponse()

def create_thread(name):
	thread=backgroundThread(name)
	thread.start()
	return

def generated(request):
		model=0
		threads=[]
		lyrics_list=[]
		context=RequestContext(request)
		strength=request.GET['strength']
		artist_names=request.GET['artist_names']
		artist_names=set(artist_names.split(','))
		for name in artist_names:
			artist_name=name.lower()
			try:
				model=Artist.objects.get(name=artist_name)
			except Artist.DoesNotExist:
				create_thread(artist_name)
				print "not exist"
				return HttpResponse(json.dumps(unicode(artist_name),ensure_ascii=False).encode('utf8'))
			print model
			lyrics_list+=list(json.loads(model.lyric_list))
		existing=Generator(lyrics_list)
		lyrics=existing.generate(250,int(strength))
		lyrics=json.dumps(unicode(lyrics),ensure_ascii=False).encode('utf8')
		return HttpResponse(lyrics)



# Create your views here.
