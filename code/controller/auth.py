import sys

import models
from database import engine, Base, get_db
from exeptions import token_exception, get_user_exception
from schemas.auth import CreateUser

sys.path.append("..")
from fastapi import Depends, APIRouter
from typing import Optional

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY3Mzk2NzE2MSwiaWF0IjoxNjczOTY3MTYxfQ.cgXhCGZvT99FFVHdHEbDhyvvEwu3Z3uFxYMNgxWkNmU'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='api/auth/token')

auth_router = APIRouter(
    prefix='/api/auth',
    tags=['authentication'],
    responses={401: {"user": "Not authorized"}}
)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

Base.metadata.create_all(bind=engine)


def get_password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hash_password):
    return bcrypt_context.verify(plain_password, hash_password)


def authenticate_user(username: str, password: str, db):
    user = db.query(models.User) \
        .filter(models.User.username == username) \
        .first()

    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(username: str, user_id: int,
                        expires_delta: Optional[timedelta] = None):
    encode = {'sub': username, 'id': user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise get_user_exception()
        return {"username": username, "id": user_id}
    except JWTError:
        raise get_user_exception()


@auth_router.post("/create/user")
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = models.User()
    create_user_model.email = create_user.email
    create_user_model.username = create_user.username
    create_user_model.first_name = create_user.first_name
    create_user_model.last_name = create_user.last_name

    hash_password = get_password_hash(create_user.password)

    create_user_model.password = hash_password
    create_user_model.is_active = True

    db.add(create_user_model)
    db.commit()
    return create_user_model


@auth_router.post('/token')
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username,
                                user.id,
                                expires_delta=token_expires)
    return {'access_token': token}
