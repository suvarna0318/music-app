"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from music_collection import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register,name="register"),
    path('search/',views.search,name="search"),
    path('song/',views.song_list,name="song_list"),
    path('details/<int:pk>/',views.details,name="details"),
    path('prev_song/<int:pk>/',views.prev_song,name="prev_song"),
    path('next_song/<int:pk>/',views.next_song,name="next_song"),
    path('album/',views.album,name="album"),
    path('artist/',views.artist,name="artist"),
    path('playlist_display/',views.playlist_display,name="playlist_display"),
    path('playlist_new/',views.playlist_new,name="playlist_new"),
    path('playlist_songs/<int:id>/',views.playlist_songs,name="playlist_songs"),
    path('login/',auth_views.LoginView.as_view(template_name="music_collection/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="music_collection/logout.html"),name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
