# Generated by Django 5.0.1 on 2024-01-23 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_playlist_delete_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='id_music',
            new_name='id_music_deezer',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='singer_name',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='song_name',
        ),
    ]
