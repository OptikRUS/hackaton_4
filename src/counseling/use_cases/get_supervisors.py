from tortoise.queryset import QuerySet

from ..repos import Supervisor, SupervisorRepo, SupervisionRepo


class GetSupervisorListCase:
    """
    Кейс получения списка КНО
    """
    def __init__(
            self,
            supervisor_repo: type[SupervisorRepo],
            supervision_repo: type[SupervisionRepo],
    ) -> None:
        self.supervisor_repo: SupervisorRepo = supervisor_repo()
        self.supervision_repo: SupervisionRepo = supervision_repo()

    async def __call__(self) -> list[Supervisor]:
        supervision_qs: QuerySet = self.supervision_repo.list()
        supervisors: list[Supervisor] = await self.supervisor_repo.list(
            prefetch_fields=[
                dict(relation="supervisions", queryset=supervision_qs, to_attr="visions")
            ]
        )
        return supervisors
