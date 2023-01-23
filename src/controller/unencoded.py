import urllib
from urllib import parse

from fastapi import APIRouter

decode_router = APIRouter(
    prefix="/api/decode",
    tags=["decode"],
    responses={404: {"description": "Not found"}},
)


@decode_router.get("/")
async def decode(url):
    return urllib.parse.quote(url, safe="")
