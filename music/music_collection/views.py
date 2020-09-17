from django.shortcuts import render
from .models import Song,Artist

# Create your views here.


def index(request):
	all_song=Song.objects.all()
	context={
	'songs':all_song,
	}
	return render(request,'music_collection/all_song.html',context)

def song_list(request):
	all_song=Song.objects.all()
	context={
	'songs':all_song,
	}
	return render(request,'music_collection/all_song.html',context)

def details(request):
	
	return render(request,'music_collection/details.html')

def album(request):
	# all_song=Song.objects.all()
	# context={
	# 'songs':all_song,
	# }
	return render(request,'music_collection/album.html')

def artist(request):
	artists=Artist.objects.all()
	context={
	'artists':artists,
	}
	return render(request,'music_collection/artist_list.html',context)