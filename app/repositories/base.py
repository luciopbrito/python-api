from abc import ABC, abstractstaticmethod
from typing import Generic, TypeVar, Sequence
from sqlalchemy.orm import Session

T = TypeVar("T")

class BaseRepository(ABC, Generic[T]):
  def __init__(self, session: Session):
    self.session = session

  @staticmethod
  def get(self, id: int) -> T | None: ...
  
  @staticmethod
  def add(self, obj: T) -> T: ...
  
  @staticmethod
  def list_all(self) -> Sequence[T]: ...
  
  @staticmethod
  def delete(self, id: int) -> None: ...