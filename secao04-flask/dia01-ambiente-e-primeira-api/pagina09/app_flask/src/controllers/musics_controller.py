from flask import Blueprint, jsonify, request
from models.music_model import MusicModel


music_controller = Blueprint("musics", __name__)


@music_controller.route("/", methods=["POST"])
def music_post():
    try:
        new_music = MusicModel(request.json)
        new_music.save()

        return jsonify(new_music.to_dict()), 201
    except Exception:
        return jsonify("404 erro no servidor"), 404


@music_controller.route("/random", methods=["GET"])
def get_random_music():
    try:
        random_music = MusicModel.get_radom()
        if not random_music:
            return jsonify(random_music.to_dict()), 204
        return jsonify(random_music.to_dict()), 200
    except Exception:
        return jsonify("404 erro no servidor"), 404
