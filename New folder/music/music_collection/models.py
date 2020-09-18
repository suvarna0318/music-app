from django.db import models

# Create your models here.
GENER_CHOICES=(
	('Rock','Rock'),
	('pop','pop'),
	('hip hop','hip,hop'),
	('country','country'),
	('classical','classcical'),

	)

class Artist(models.Model):
	name=models.CharField(max_length=200)
	image=models.ImageField(upload_to="images")

	def __str__(self):
		return self.name
class Song(models.Model):
    title = models.CharField(max_length=200, verbose_name="Song name")
    cover_img = models.ImageField(upload_to="song_cover_img", blank=False)
    song = models.FileField(upload_to='song_directory_path')
    genre = models.CharField(max_length=100,choices=GENER_CHOICES)
    artists = models.ForeignKey(Artist,on_delete=models.CASCADE)


    def __str__(self):
    	return self.title