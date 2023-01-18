from fastapi import Depends

from controller.auth import get_current_user, get_user_exception
from repositories.post import PostRepository
from schemas.post import Post


class PostService:
    def __init__(self, repository: PostRepository = Depends(), user: dict = Depends(get_current_user)):
        self.repository = repository
        self.user = user

    def get_posts(self):
        if self.user is None:
            raise get_user_exception()
        return self.repository.get_posts()

    def read_post(self, post_id):
        if self.user is None:
            raise get_user_exception()
        return self.repository.read_post(post_id)

    def create_post(self, post: Post):
        if self.user is None:
            raise get_user_exception()
        return self.repository.create_post(post)
