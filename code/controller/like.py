import sys

from controller.auth import get_current_user, get_user_exception
from database import SessionLocal, engine

sys.path.append("..")

import models

from fastapi import Depends, APIRouter, HTTPException

from sqlalchemy.orm import Session
from pydantic import BaseModel

like_router = APIRouter(
    prefix='/api/like',
    tags=['like'],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Like(BaseModel):
    user_id: int
    post_id: int


@like_router.get('/')
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Like).all()


@like_router.post("/")
async def create_like(like: Like,
                      user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    like_model = models.Like()
    like_model.user_id = like.user_id
    like_model.post_id = like.post_id

    if like_model.user_id == get_current_user():
        print("Лайки себе ставить нельзя")

    db.add(like_model)
    db.commit()

    return successful_response(201)


def successful_response(status_code: int):
    return {
        'status': status_code,
        'transaction': 'Successful'
    }


def http_exception():
    return HTTPException(status_code=404, detail='Todo not found')
