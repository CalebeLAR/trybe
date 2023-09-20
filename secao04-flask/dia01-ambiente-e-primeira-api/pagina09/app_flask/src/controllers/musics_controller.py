from flask import Blueprint, jsonify, request
from models.music_model import MusicModel


music_controller = Blueprint("musics", __name__)


@music_controller.route("/", methods=["POST"])
def music_post():
    new_music = MusicModel(request.json)
    new_music.save()

    return jsonify(new_music.to_dict()), 200
