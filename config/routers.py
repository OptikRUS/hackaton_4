from fastapi import APIRouter


def get_routers() -> list[APIRouter]:
    from src.users.api import users_router
    from src.admins.api import admins_router

    routers: list[APIRouter] = list()

    routers.append(users_router)
    routers.append(admins_router)

    return routers
