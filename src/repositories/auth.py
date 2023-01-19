# import sys
# from datetime import timedelta
#
# from passlib.context import CryptContext
#
# from .. import models
# from ..exeptions import token_exception
# from ..services.auth import get_password_hash
#
# sys.path.append("..")
#
#
# from ..repositories.base_repository import BaseRepository
#
# bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
#
#
#
# class CreateUserRepository(BaseRepository):
#     def get_password_hash(self, password):
#         return bcrypt_context.hash(password)
#
#     def creat_new_user(self, create_user):
#         create_user_model = models.User()
#         create_user_model.email = create_user.email
#         create_user_model.username = create_user.username
#         create_user_model.first_name = create_user.first_name
#         create_user_model.last_name = create_user.last_name
#
#         hash_password = get_password_hash(create_user.password)
#
#         create_user_model.password = hash_password
#         create_user_model.is_active = True
#
#         self.db.add(create_user_model)
#         self.db.commit()
#         return create_user_model
#
#
#     def login_for_access_token(form_data):
#         user = authenticate_user(form_data.username, form_data.password, self.db)
#         if not user:
#             raise token_exception()
#         token_expires = timedelta(minutes=20)
#         token = create_access_token(user.username,
#                                     user.id,
#                                     expires_delta=token_expires)
#         return {'access_token': token}
#
#
#
#
#
#
#
# def verify_password(plain_password, hash_password):
#     return bcrypt_context.verify(plain_password, hash_password)
#
#
# def authenticate_user(username: str, password: str, db):
#     user = db.query(models.User) \
#         .filter(models.User.username == username) \
#         .first()
#
#     if not user:
#         return False
#     if not verify_password(password, user.password):
#         return False
#     return user
#
#
# def create_access_token(username: str, user_id: int,
#                         expires_delta: Optional[timedelta] = None):
#     encode = {'sub': username, 'id': user_id}
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     encode.update({"exp": expire})
#     return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
