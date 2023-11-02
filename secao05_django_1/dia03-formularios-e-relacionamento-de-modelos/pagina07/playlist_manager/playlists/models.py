# playlists/models.py
from django.db import models

from playlists.validators import (
    validate_music_length,
    validate_name,
    validate_singer_name,
)


class Singer(models.Model):
    name = models.CharField(max_length=50, validators=[validate_singer_name])

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=50, validators=[validate_name])
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=50)
    recorded_at = models.DateField()
    length_in_seconds = models.IntegerField(validators=[validate_music_length])

    def __str__(self):
        return self.name
