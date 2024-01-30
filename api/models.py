from django.db import models

# Create your models here.
class PlayList(models.Model):
    id_user = models.IntegerField()
    id_music_deezer = models.BigIntegerField()