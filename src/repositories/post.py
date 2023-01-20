from src import models
from src.schemas.post import Post
from src.shared.exeptions import http_post_exception
from src.shared.responses import successful_response
from ..repositories.base_repository import BaseRepository


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

    def update_post(self, post_id, post: Post):
        post_model = self.db.query(models.Post).filter(models.Post.id == post_id).first()

        if post_model is None:
            raise http_post_exception()

        post_model.content = post.content

        self.db.add(post_model)
        self.db.commit()

        return successful_response(200)

    def delete_post(self, post_id):
        post_model = self.db.query(models.Post).filter(models.Post.id == post_id).first()
        if post_model is None:
            raise http_post_exception()

        self.db.query(models.Post) \
            .filter(models.Post.id == post_id) \
            .delete()

        self.db.commit()

        return successful_response(200)
