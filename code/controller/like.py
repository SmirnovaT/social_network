import sys

from database import engine, Base
from schemas.like import Like
from services.like import LikeService

sys.path.append("..")

from fastapi import Depends, APIRouter

like_router = APIRouter(
    prefix='/api/like',
    tags=['like'],
    responses={404: {"description": "Not found"}}
)

Base.metadata.create_all(bind=engine)


@like_router.get('/')
async def read_all(service: LikeService = Depends(LikeService)):
    return service.get_like()


@like_router.post("/")
async def create_like(like: Like, service: LikeService = Depends(LikeService)):
    return service.create_like(like)
