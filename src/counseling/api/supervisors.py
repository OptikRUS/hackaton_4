from fastapi import APIRouter

from ..use_cases import GetSupervisorListCase
from ..repos import SupervisorRepo, SupervisionRepo
from ..models import SupervisorResponse

router: APIRouter = APIRouter(prefix="/supervisors", tags=["supervisors"])


@router.get(
    "/list",
    response_model=list[SupervisorResponse],
)
async def get_supervisors_list_view():
    """
    Получение списка КНО
    """
    resources: dict = dict(
        supervisor_repo=SupervisorRepo,
        supervision_repo=SupervisionRepo,
    )
    get_supervisors: GetSupervisorListCase = GetSupervisorListCase(**resources)
    return await get_supervisors()
