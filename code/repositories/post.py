import models
from exeptions import http_post_exception

from repositories.base_repository import BaseRepository
from responses import successful_response
from schemas.post import Post


class PostRepository(BaseRepository):

    def get_posts(self):
        return self.db.query(models.Post).all()

    def read_post(self, post_id):
        post_model = self.db.query(models.Post) \
            .filter(models.Post.id == post_id) \
            .first()

        if post_model is not None:
            return post_model
        raise http_post_exception()

    def create_post(self, post: Post):
        post_model = models.Post()
        post_model.content = post.content

        self.db.add(post_model)
        self.db.commit()

        return successful_response(201)
