from typing import Generic, TypeVar

Data = TypeVar("Data")
Result = TypeVar("Result")


class Interactor(Generic[Data, Result]):
    async def __call__(self, data: Data) -> Result:
        raise NotImplementedError
