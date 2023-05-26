from ..entities import BaseCounselingModel


class Supervision(BaseCounselingModel):
    id: int
    name: str


class SupervisorResponse(BaseCounselingModel):
    id: int
    name: str
    visions: list[Supervision]

    class Config:
        orm_mode = True
