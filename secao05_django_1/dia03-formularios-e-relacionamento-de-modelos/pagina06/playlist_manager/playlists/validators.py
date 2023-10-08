# playlists/validators.py

import re
from django.core.exceptions import ValidationError


def validate_music_length(value):
    if value not in range(1, 3601):
        raise ValidationError(
            "A duração da música deve ser um número"
            " inteiro entre 1 e 3600 segundos. O valor "
            "{value} não é válido."
        )


def validate_name(value):
    if not re.search(r'\d', value):
        raise ValidationError(
            "O nome do cantor não pode conter digitos com em {value}"
        )
