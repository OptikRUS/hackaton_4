from fastapi import APIRouter


def get_routers() -> list[APIRouter]:
    from src.users.api import users_router
    from src.counseling.api import slots_router, supervisors_router, topics_router, chat_bot_router
    from src.meetings.api import meetings_router

    routers: list[APIRouter] = list()

    routers.append(users_router)
    routers.append(slots_router)
    routers.append(supervisors_router)
    routers.append(topics_router)
    routers.append(meetings_router)
    routers.append(chat_bot_router)

    return routers
