# flake8: noqa
from django import forms
from playlists.validators import validate_music_length, validate_singer_name ,validate_name
from playlists.models import Music, Singer


class CreateMusicForm(forms.Form):
    name = forms.CharField(
        max_length=50,
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
        validators=[validate_music_length,],
        label="Duração em segundos",
        min_value=1,
        max_value=3600,
    )


class CreateMusicModelForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Nome da música"
        self.fields["recorded_at"].label = "Data de gravação"
        self.fields["recorded_at"].widget = forms.DateInput(
                attrs={"type": "date"})
        self.fields["recorded_at"].initial = "2023-07-06"
        self.fields["length_in_seconds"].label = "Duração em segundos"
        self.fields["singer"].label = "Artista"
        self.fields["singer"].widget = forms.Select(
            choices=[
                (singer.id, singer.name)
                for singer in Singer.objects.filter(name__contains="a")
            ]
        )


class CreatePlaylistForm(forms.Form):
    name = forms.CharField(max_length=50, validators=[validate_name])
    is_active = forms.BooleanField()


class CreateSingerForm(forms.Form):
    name = forms.CharField(max_length=50, validators=[validate_singer_name])
