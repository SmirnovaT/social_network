from fastapi import FastAPI

import models
from controller import post, like, auth
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(post.post_router)
app.include_router(like.like_router)
app.include_router(auth.auth_router)
