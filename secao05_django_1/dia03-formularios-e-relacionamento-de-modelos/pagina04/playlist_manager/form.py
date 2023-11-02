# flake8: noqa

import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "playlist_manager.settings")
django.setup()

from playlists.forms import CreatePlaylistForm, CreateSingerForm

form = CreatePlaylistForm({})  # formulário instanciado com um dicionário vazio
form.is_valid()  # retorna False
form.errors  # retorna {'name': ['Este campo é obrigatório.'], 'is_active': ['Este campo é obrigatório.']}

form_2 = CreatePlaylistForm(
    {
        "name": "Essa playlist tem um nome com mais de cinquenta caracteres, o que você acha que vai acontecer?",
        "is_active": True,
    }
)
form_2.is_valid()  # retorna False
form_2.errors  # retorna {'name': ['Certifique-se de que o valor tenha no máximo 50 caracteres (ele possui 94).']}

form_3 = CreatePlaylistForm({"name": "Playlist de Estudo", "is_active": True})
form_3.is_valid()  # retorna True
print(form_3.errors)
form_3.errors  # retorna {}

unbound_form = CreatePlaylistForm()  #  formulário não vinculado
unbound_form.is_valid()  #  retorna False
unbound_form.errors  #  retorna {} Esse tipo de formulário não passa por validação

# Exercício01
formSinger = CreateSingerForm({"name": "Juan"})
