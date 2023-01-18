from fastapi import Depends
from controller.auth import get_current_user, get_user_exception
from exeptions import http_like_exception
from repositories.like import LikeRepository
from schemas.like import Like


class LikeService:
    def __init__(self, repository: LikeRepository = Depends(), user: dict = Depends(get_current_user)):
        self.repository = repository
        self.user = user

    def get_like(self):
        if self.user is None:
            raise get_user_exception()
        return self.repository.get_like()

    def create_like(self, like: Like):
        if self.user is None:
            raise get_user_exception()
        if self.user['id'] == like.user_id:
            raise http_like_exception()
        return self.repository.create_like(like)
