from typing import Sequence
from sqlalchemy import select
from app.models.pedido import Pedido
from app.repositories.base import BaseRepository

class PedidoRepository(BaseRepository[Pedido]):
  model = Pedido

  def get(self, id) -> Pedido | None:
    return self.session.get(self.model, id)

  def add(self, obj: Pedido) -> Pedido:
    self.session.add(obj)
    self.session.commit()
    self.session.refresh(obj)
    return obj

  def list_all(self) -> Sequence[Pedido]:
    return self.session.execute(select(self.model)).scalars().all()

  def delete(self, id: int) -> None: 
    obj = self.get(id)
    if obj:
      self.session.delete(obj)
      self.session.commit()