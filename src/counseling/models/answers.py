from haystack.schema import Answer, Document

from ..entities import BaseCounselingModel


class AnswerListResponse(BaseCounselingModel):
    # query: str
    # answers: list[Answer]
    documents: list[Document]
    # no_ans_gap: float
