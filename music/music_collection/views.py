from django.shortcuts import render
from .models import Song,Artist

# Create your views here.


def index(request):
	# all_song=Song.objects.all()
	song=Song.objects.get(id=3)
	context={
	# 'songs':all_song,
	'song':song,
	}
	return render(request,'music_collection/all_song.html',context)

def song_list(request):
	all_song=Song.objects.all()
	context={
	'songs':all_song,
	}
	return render(request,'music_collection/all_song.html',context)

def details(request,pk):
	song=Song.objects.get(id=pk)
	context={
	'song':song,
	}
	
	return render(request,'music_collection/details.html',context)

def prev_song(request,pk):
	print(pk)
	pk=pk-1
	print(pk)
	song=Song.objects.get(id=pk)
	context={
	'song':song,
	}
	
	return render(request,'music_collection/details.html',context)
def next_song(request,pk):
	pk=pk+1
	song=Song.objects.get(id=pk)
	context={
	'song':song,
	}
	
	return render(request,'music_collection/details.html',context)


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