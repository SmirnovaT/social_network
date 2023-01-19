# from fastapi.security import OAuth2PasswordBearer
#
# from ..controller.auth import get_current_user
# from ..repositories.auth import CreateUserRepository
# import sys
#
# from .. import models
#
# sys.path.append("..")
#
# from fastapi import Depends
# from typing import Optional
# from passlib.context import CryptContext
# from datetime import datetime, timedelta
# from jose import jwt, JWTError
#
# SECRET_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY3Mzk2NzE2MSwiaWF0IjoxNjczOTY3MTYxfQ.cgXhCGZvT99FFVHdHEbDhyvvEwu3Z3uFxYMNgxWkNmU'
# ALGORITHM = 'HS256'
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
#
# oauth2_bearer = OAuth2PasswordBearer(tokenUrl='api/auth/token')
#
#
# class CreateUserService:
#     def __init__(self, repository: CreateUserRepository = Depends(), user: dict = Depends(get_current_user)):
#         self.repository = repository
#         self.user = user
#
#     def create_new_user(self, create_user):
#         return self.repository.creat_new_user(create_user)
#
#     def login_for_access_token(self, form_data):
#         return self.user.login_for_access_token(form_data)
#



