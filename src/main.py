from fastapi import FastAPI

from src.controller import post, like, auth
from src.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(post.post_router)
app.include_router(like.like_router)
app.include_router(auth.auth_router)
