from django.shortcuts import render,redirect
from .models import Song,Artist,UserPlaylist
from .forms import RegisterForm,PlaylistCreationForm


# Create your views here.
def register(request):
	print("working")
	if request.method=='POST':
		u_form=RegisterForm(request.POST)
		if u_form.is_valid():
			u_form.save()
			return render(request,'music_collection/base.html')
	else:
		u_form=RegisterForm()
	context={
	'form':u_form,
	}


	return render(request,'music_collection/register.html',context)


# def index(request):
# 	# all_song=Song.objects.all()
# 	song=Song.objects.get(id=3)
# 	context={
# 	# 'songs':all_song,
# 	'song':song,
# 	}
# 	return render(request,'music_collection/all_song.html',context)

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
def search(request):
	print("working ",request.GET.get('q'))
	query=request.GET.get('q')
	search_res=Song.objects.search(query)
	context={
	'songs':search_res,
	}
	
	return render(request,'music_collection/search.html',context)


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

def playlist_new(request):
	if request.method=='POST':
		form=PlaylistCreationForm(request.POST)
		if form.is_valid():
			title=form.cleaned_data['playlist_title']
			obj=UserPlaylist.objects.create(playlist_name=title)
			obj.save()
			print("show create dplaylist")
			return redirect('playlist_display')

	else:
		form=PlaylistCreationForm()
	context={
	'form':form,
	}
	return render(request,'music_collection/playlist_new.html',context)



def playlist_display(request):
	objects=UserPlaylist.objects.all()
	context={
	'objects':objects,
	}
	return render(request,'music_collection/playlist_display.html',context)
def playlist_songs(request,id):

	obj=UserPlaylist.objects.get(pk=id)
	objects=obj.song.all()
	print(objects)
	context={
	'objects':objects,
	}
	return render(request,'music_collection/playlist_songs.html',context)


