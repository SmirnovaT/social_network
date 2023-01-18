from fastapi import FastAPI

from controller import like, post, auth
from database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(post.post_router)
app.include_router(like.like_router)
app.include_router(auth.auth_router)
