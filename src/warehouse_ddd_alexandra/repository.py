from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from . import model


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, batch: model.Batch) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, reference: str) -> model.Batch:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[model.Batch]:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def add(self, batch: model.Batch) -> None:
        self.__session.add(batch)

    def get(self, reference: str) -> model.Batch:
        batches = self.__session.query(model.Batch)
        return batches.filter_by(reference=reference).one()

    def list(self) -> list[model.Batch]:
        return self.__session.query(model.Batch).all()


class FakeRepository(AbstractRepository):
    def __init__(self, batches: list[model.Batch] = []) -> None:
        self.__batches = set(batches)

    def add(self, batch: model.Batch) -> None:
        self.__batches.add(batch)

    def get(self, reference: str) -> model.Batch:
        return [b for b in self.__batches if b.reference == reference][0]

    def list(self) -> list[model.Batch]:
        return list(self.__batches)
