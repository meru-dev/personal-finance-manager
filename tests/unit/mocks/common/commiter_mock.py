from src.application.common.ports.commiter import Commiter


class CommiterMock(Commiter):
    def __init__(self):
        self.commited = False
        self.flushed = False

    async def commit(self) -> None:
        self.commited = True

    async def flush(self) -> None:
        self.flushed = True
