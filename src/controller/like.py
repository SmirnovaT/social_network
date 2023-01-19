from src.database import engine, Base
from src.schemas.like import Like

from src.services.like import LikeService



from fastapi import Depends, APIRouter, FastAPI
app = FastAPI()
like_router = APIRouter(
    prefix='/api/like',
    tags=['like'],
    responses={404: {"description": "Not found"}}
)

Base.metadata.create_all(bind=engine)


@like_router.get('/')
async def read_all(service: LikeService = Depends(LikeService)):
    return service.get_like()


@like_router.post("/")
async def create_like(like: Like, service: LikeService = Depends(LikeService)):
    return service.create_like(like)
