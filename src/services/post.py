from fastapi import Depends

from src.repositories.post import PostRepository
from src.schemas.post import Post
from src.services.auth import get_current_user
from src.shared.exeptions import get_user_exception


class PostService:
    def __init__(
        self,
        repository: PostRepository = Depends(),
        user: dict = Depends(get_current_user),
    ):
        self.repository = repository
        self.user = user

    def get_posts(self):
        self.user_none()
        return self.repository.get_posts()

    def read_post(self, post_id):
        self.user_none()
        return self.repository.read_post(post_id)

    def create_post(self, post: Post):
        self.user_none()
        return self.repository.create_post(post)

    def update_post(self, post_id, post: Post):
        self.user_none()
        return self.repository.update_post(post_id, post)

    def delete_post(self, post_id):
        self.user_none()
        return self.repository.delete_post(post_id)

    def user_none(self):
        if self.user is None:
            raise get_user_exception()
