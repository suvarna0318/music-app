from django.shortcuts import render,redirect
from .models import Song,Artist,UserPlaylist
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


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

def song_list(request):
	all_song=Song.objects.all()
	context={
	'songs':all_song,
	'song':all_song[0],
	}
	return render(request,'music_collection/all_song.html',context)

def song_list_with_id(request,id):
	all_song=Song.objects.all()
	song=Song.objects.get(id=id)
	context={
	'songs':all_song,
	'song':song,
	}
	return render(request,'music_collection/all_song.html',context)

def details(request,pk):
	song=Song.objects.get(id=pk)
	context={
	'song':song,
	}
	
	return render(request,'music_collection/details.html',context)
def search(request):
	
	query=request.GET.get('q')
	q_list=query.split(" ")
	print(q_list)
	ignore_list=['by','and','song','songs']
	for i in ignore_list:
		if i in q_list:
			q_list.remove(i)

	print(q_list)

	query=str(" ".join(q_list))
	print(query)
	search_res=Song.objects.search(query)
	context={
	'songs':search_res,
	}
	
	return render(request,'music_collection/search.html',context)


def prev_song(request,pk):
	songs=Song.objects.all()
	print(pk)
	pk=pk-1
	print(pk)
	song=Song.objects.get(id=pk)
	context={
	'songs':songs,
	'song':song,
	}
	
	return render(request,'music_collection/all_song.html',context)
def next_song(request,pk):
	songs=Song.objects.all()
	pk=pk+1
	song=Song.objects.get(id=pk)
	context={
	'songs':songs,
	'song':song,
	}
	
	return render(request,'music_collection/all_song.html',context)


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
	return render(request,'music_collection/right_click_menu.html')
@login_required(login_url='/login/')
def playlist_new(request):
	if request.method=='POST':
		
		title=request.POST.get('playlist_name')
		print(title)

		if title!="":
			print("context:",title)
			obj=UserPlaylist.objects.create(playlist_name=title,user=request.user)
			obj.save()
			print("show created playlist")
			return redirect('playlist_display')
		else:
			obj=UserPlaylist.objects.create(playlist_name='NewPlaylist',user=request.user)
			obj.save()
			print("show created playlist")
			return redirect('playlist_display')


@login_required(login_url='/login/')
def playlist_display(request):
	objects=UserPlaylist.objects.filter(user=request.user)
	# print(request.user)
	context={
	'objects':objects,
	}
	return render(request,'music_collection/playlist_display.html',context)
@login_required(login_url='/login/')
def playlist_songs(request,id):

	obj=UserPlaylist.objects.get(pk=id)
	objects=obj.song.all()
	print(objects)
	context={
	'objects':objects,
	}
	return render(request,'music_collection/playlist_songs.html',context)


