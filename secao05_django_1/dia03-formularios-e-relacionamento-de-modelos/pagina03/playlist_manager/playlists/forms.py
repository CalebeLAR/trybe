# flake8: noqa
from django import forms
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "playlist_manager.settings")
django.setup()

class CreateMusicForm(forms.Form):
    name = forms.CharField(max_length=50)
    recorded_at = forms.DateField()
    length_in_seconds = forms.IntegerField()


class CreatePlaylistForm(forms.Form):
    name = forms.CharField(max_length=50)
    is_active = forms.BooleanField()


form = CreatePlaylistForm()
form.is_bound # retorna False

form = CreatePlaylistForm({"name":"Playlist de Estudo", "is_active": True})
form.is_bound # retorna True