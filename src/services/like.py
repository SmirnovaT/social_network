from fastapi import Depends
from src.controller.auth import get_current_user, get_user_exception
from src.exeptions import http_like_exception
from src.repositories.like import LikeRepository
from src.schemas.like import Like


class LikeService:
    def __init__(self, repository: LikeRepository = Depends(), user: dict = Depends(get_current_user)):
        self.repository = repository
        self.user = user

    def get_like(self):
        self.user_none()
        return self.repository.get_like()

    def create_like(self, like: Like):
        self.user_none()
        if self.user['id'] == like.user_id:
            raise http_like_exception()
        return self.repository.create_like(like)

    def user_none(self):
        if self.user is None:
            raise get_user_exception()
