from fastapi import Depends, APIRouter, FastAPI

from src.schemas.like import Like
from src.services.like import LikeService

app = FastAPI()
like_router = APIRouter(
    prefix="/api/like", tags=["like"], responses={404: {"description": "Not found"}}
)


@like_router.get("/")
async def read_all(service: LikeService = Depends(LikeService)):
    return service.get_like()


@like_router.post("/")
async def create_like(like: Like, service: LikeService = Depends(LikeService)):
    return service.create_like(like)
