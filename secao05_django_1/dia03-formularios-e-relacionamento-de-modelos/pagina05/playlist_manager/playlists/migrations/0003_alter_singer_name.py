# Generated by Django 4.2.5 on 2023-10-07 19:24

from django.db import migrations, models
import playlists.validators


class Migration(migrations.Migration):
    dependencies = [
        ("playlists", "0002_alter_music_length_in_seconds"),
    ]

    operations = [
        migrations.AlterField(
            model_name="singer",
            name="name",
            field=models.CharField(
                max_length=50, validators=[playlists.validators.validate_singer_name]
            ),
        ),
    ]
