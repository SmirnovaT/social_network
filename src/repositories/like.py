import sys

from src import models

sys.path.append("../../code")
from src.models.like import Like

from ..repositories.base_repository import BaseRepository
from src.shared.responses import successful_response


class LikeRepository(BaseRepository):

    def get_like(self):
        return self.db.query(models.Like).all()

    def create_like(self, like: Like):
        like_model = models.Like()
        like_model.user_id = like.user_id
        like_model.post_id = like.post_id

        self.db.add(like_model)
        self.db.commit()

        return successful_response(201)
