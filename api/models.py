from django.db import models

# Create your models here.
class PlayList(models.Model):
    id_user = models.IntegerField()
    id_music = models.IntegerField()
    singer_name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)