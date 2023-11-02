# playlists/validators.py
from django.core.exceptions import ValidationError


def validate_music_length(value):
    if value not in range(1, 3601):
        raise ValidationError(
            "A duração da música deve ser um número"
            " inteiro entre 1 e 3600 segundos. O valor "
            f"{value} não é válido."
        )


def validate_name(value):
    if any(char.isdigit() for char in value):
        raise ValidationError(f"O nome não pode conter números. {value}")


def validate_singer_name(value):
    if any(char.isdigit() for char in value):
        raise ValidationError(f"O nome do cantor não pode conter digitos: {value}")
