from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from common.security import UserAuth, UserLogin, Token, UserType
from ..repos import User
from ..models import UserRegisterRequest, UserRegisterResponse, UserResponse, UserUpdateRequest
from ..use_cases import UserRegistration, UpdateUserProfile
from ..exceptions import BaseUserExceptionModel

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/register",
    status_code=201,
    response_model=UserRegisterResponse,
    responses={
        409: {"model": BaseUserExceptionModel}
    }
)
async def register_user(user: UserRegisterRequest):
    """
    Регистрация пользователя
    """
    user_register: UserRegistration = UserRegistration()
    return await user_register(user)


@router.post(
    "/login",
    status_code=200,
    response_model=Token,
    responses={
        401: {"model": BaseUserExceptionModel}
    }
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Авторизация пользователя
    """
    access_token: UserLogin = UserLogin(form_data.username, form_data.password)
    return await access_token()


@router.get("/me", status_code=200, response_model=UserResponse)
async def get_me(current_user: User = Depends(UserAuth(UserType.ANY))):
    """
    Получить информацию о себе
    """
    return current_user


@router.put(
    "/update_user",
    response_model=UserResponse,
)
async def update_me(user: UserUpdateRequest, current_user: User = Depends(UserAuth(UserType.ANY))):
    """
    Изменение профиля пользователя
    """
    user_update: UpdateUserProfile = UpdateUserProfile(current_user)
    return await user_update(user_data=user)
