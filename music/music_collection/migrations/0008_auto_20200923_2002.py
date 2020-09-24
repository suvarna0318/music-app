# Generated by Django 3.0.8 on 2020-09-23 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_collection', '0007_userplaylist_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='lang',
            field=models.CharField(choices=[('kannada', 'kannada'), ('hindi', 'hindi'), ('english', 'english'), ('tamil', 'tamil')], default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userplaylist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]