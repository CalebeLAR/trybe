# flake8: noqa
from django import forms
from playlists.validators import validate_music_length, validate_name


class CreateMusicForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        validators=[validate_name],
        help_text= "<-- digite aqui",
        label="Nome da música",
        strip=True,
    )
    recorded_at = forms.DateField(
        label="Data de gravação",
        widget=forms.DateInput(attrs={"type": "date"}),
        initial="2023-07-10",
    )
    length_in_seconds = forms.IntegerField(
        validators=[validate_music_length],
        label="Duração em segundos",
        min_value=1,
        max_value=3600,
    )


class CreatePlaylistForm(forms.Form):
    name = forms.CharField(max_length=50)
    is_active = forms.BooleanField()


class CreateSingerForm(forms.Form):
    name = forms.CharField(max_length=50, validators=[validate_name])
