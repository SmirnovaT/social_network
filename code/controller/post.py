import sys

from database import SessionLocal, engine

sys.path.append("..")

import models

from fastapi import Depends, HTTPException, APIRouter

from sqlalchemy.orm import Session
from pydantic import BaseModel

post_router = APIRouter(
    prefix='/api/post',
    tags=['post'],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Post(BaseModel):
    content: str


@post_router.get('/')
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Post).all()


@post_router.get('/{post_id}')
async def read_post(post_id: int,
                    db: Session = Depends(get_db)):
    post_model = db.query(models.Post) \
        .filter(models.Post.id == post_id) \
        .first()

    if post_model is not None:
        return post_model
    raise http_exception()


@post_router.post('/')
async def create_post(post: Post, db: Session = Depends(get_db)):
    post_model = models.Post()
    post_model.content = post.content

    db.add(post_model)
    db.commit()

    return successful_response(201)


@post_router.put('/{post_id}')
async def update_post(post_id: int, post: Post, db: Session = Depends(get_db)):
    post_model = db.query(models.Post).filter(models.Post.id == post_id).first()

    if post_model is None:
        raise http_exception()

    post_model.content = post.content

    db.add(post_model)
    db.commit()

    return successful_response(200)


@post_router.delete('/{post_id}')
async def delete_todo(post_id: int,
                      db: Session = Depends(get_db)):
    post_model = db.query(models.Post).filter(models.Post.id == post_id).first()

    if post_model is None:
        raise http_exception()

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


def http_exception():
    return HTTPException(status_code=404, detail='Todo not found')
