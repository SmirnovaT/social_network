from fastapi import Depends, APIRouter, FastAPI

from src.database import engine, Base
from src.schemas.post import Post
from src.services.post import PostService

app = FastAPI()

post_router = APIRouter(
    prefix='/api/post',
    tags=['post'],
    responses={404: {"description": "Not found"}}
)

Base.metadata.create_all(bind=engine)


@post_router.get('/')
async def read_all(service: PostService = Depends(PostService)):
    return service.get_posts()


@post_router.get('/{post_id}')
async def read_post(post_id: int, service: PostService = Depends(PostService)
                    ):
    return service.read_post(post_id)


@post_router.post('/')
async def create_post(post: Post, service: PostService = Depends(PostService)):
    return service.create_post(post)


@post_router.put('/{post_id}')
async def update_post(post_id: int, post: Post, service: PostService = Depends(PostService)):
    return service.update_post(post_id, post)


@post_router.delete('/{post_id}')
async def delete_post(post_id: int, service: PostService = Depends(PostService)):
    return service.delete_post(post_id)
