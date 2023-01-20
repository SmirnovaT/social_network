from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from src.schemas.auth import CreateUser
from src.services.auth import CreateUserService

auth_router = APIRouter(
    prefix="/api/auth",
    tags=["authentication"],
    responses={401: {"user": "Not authorized"}},
)


@auth_router.post("/create/user")
async def create_new_user(
    create_user: CreateUser, service: CreateUserService = Depends(CreateUserService)
):
    return service.create_new_user(create_user)


@auth_router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: CreateUserService = Depends(CreateUserService),
):
    return service.login_for_access_token(form_data)
