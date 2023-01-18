import sys

from controller.auth import get_current_user, get_user_exception
from database import engine, Base, get_db
from schemas.post import Post
from services.post import PostService

sys.path.append("..")

import models

from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

post_router = APIRouter(
    prefix='/api/post',
    tags=['post'],
    responses={404: {"description": "Not found"}}
)

Base.metadata.create_all(bind=engine)


@post_router.get('/')
async def read_all(service: PostService = Depends(PostService)):
    return service.get_posts()


@post_router.get('/{post_id}')
async def read_post(post_id: int, service: PostService = Depends(PostService)
                    ):
    return service.read_post(post_id)


@post_router.post('/')
async def create_post(post: Post, service: PostService = Depends(PostService)):
    return service.create_post(post)


@post_router.put('/{post_id}')
async def update_post(post_id: int, post: Post, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    post_model = db.query(models.Post).filter(models.Post.id == post_id).first()

    if user is None:
        raise get_user_exception()

    if post_model is None:
        raise http_post_exception()

    post_model.content = post.content

    db.add(post_model)
    db.commit()

    return successful_response(200)


@post_router.delete('/{post_id}')
async def delete_todo(post_id: int, user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    post_model = db.query(models.Post).filter(models.Post.id == post_id).first()

    if user is None:
        raise get_user_exception()
    if post_model is None:
        raise http_post_exception()

    db.query(models.Post) \
        .filter(models.Post.id == post_id) \
        .delete()

    db.commit()

    return successful_response(200)


def successful_response(status_code: int):
    return {
        'status': status_code,
        'transaction': 'Successful'
    }
