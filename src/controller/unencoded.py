import urllib
from urllib import parse

from fastapi import APIRouter

unencoded_router = APIRouter(
    prefix="/api/unencoded",
    tags=["unencoded"],
    responses={404: {"description": "Not found"}},
)


@unencoded_router.get("/")
async def unencoded(url):
    return urllib.parse.quote(url, safe="")
