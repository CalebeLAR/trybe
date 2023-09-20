# music_model
from .db import db
import random
from .abstract_model import AbstractModel


class MusicModel(AbstractModel):
    _collection = db["musics"]

    def __init__(self, json_data: dict):
        super().__init__(json_data)

    @classmethod
    def get_radom(cls):
        data = cls.find()
        if not data:
            return None
        return random.choice(data)

    def to_dict(self):
        return {"_id": f"{self.data['_id']}", "music": f"{self.data['music']}"}

    pass
