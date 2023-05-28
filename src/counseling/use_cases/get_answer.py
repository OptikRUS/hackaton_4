from ..services import BotAnswerService


class GetAnswerCase:
    """
    Кейс получения ответа чата
    """
    def __init__(
            self,
            bot_answer_service: type[BotAnswerService],
    ) -> None:
        self.bot_answer_service: BotAnswerService = bot_answer_service(path="/src/counseling/services/files/")

    async def __call__(self, query: str):
        answers: BotAnswerService = self.bot_answer_service.get_answer(query="Экологические нормы социальной поддержки")
        return answers
