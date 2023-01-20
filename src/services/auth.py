from datetime import timedelta, datetime
from typing import Optional

from fastapi import Depends
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from src import models
from src.core.config import SECRET_KEY, ALGORITHM, oauth2_bearer, bcrypt_context
from src.database import get_db
from src.repositories.auth import CreateUserRepository
from src.schemas.auth import CreateUser
from src.shared.exeptions import token_exception, get_user_exception


class CreateUserService:
    def __init__(self, repository: CreateUserRepository = Depends(), db: Session = Depends(get_db)):
        self.repository = repository,
        self.db = db

    def create_new_user(self, create_user: CreateUser):
        return self.repository.creat_new_user(create_user)

    def login_for_access_token(self, form_data):
        user = authenticate_user(form_data.username, form_data.password, self.db)
        if not user:
            raise token_exception()
        token_expires = timedelta(minutes=20)
        token = create_access_token(user.username,
                                    user.id,
                                    expires_delta=token_expires)
        return {'access_token': token}


def authenticate_user(username: str, password: str, db):
    user = db.query(models.User) \
        .filter(models.User.username == username) \
        .first()
    if not user:
        return False
    if not _verify_password(password, user.password):
        return False
    return user


def _verify_password(plain_password, hash_password):
    return bcrypt_context.verify(plain_password, hash_password)


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
