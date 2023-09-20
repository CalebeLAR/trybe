# music_model
from .db import db
from .abstract_model import AbstractModel


class MusicModel(AbstractModel):
    _collection = db["music"]

    def __init__(self, json_data: dict):
        super().__init__(json_data)

    def to_dict(self):
        return {
            "_id": f"{self.data['_id']}",
            "music": f"{self.data['music']}"
        }

    pass
