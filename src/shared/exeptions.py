from fastapi import HTTPException
from starlette import status


def http_like_exception():
    return HTTPException(status_code=403, detail="Нельзя ставить лайки себе")


def get_user_exception():
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return credentials_exception


def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token_exception_response


def http_post_exception():
    return HTTPException(status_code=404, detail="Post not found")
