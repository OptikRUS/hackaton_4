from ..repos import TopicRepo, Topic


class GetTopicListCase:
    """
    Кейс получения тем для консультирования
    """
    def __init__(
            self,
            topic_repo: type[TopicRepo],
    ) -> None:
        self.topic_repo: TopicRepo = topic_repo()

    async def __call__(self) -> list[Topic]:
        return await self.topic_repo.list()
