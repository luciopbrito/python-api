from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from app.models.base import Base

class Pedido(Base):
  __tablename__ = "pedidos"

  id: Mapped[int] = mapped_column(primary_key=True)
  produto: Mapped[str] = mapped_column(String(150))
  quantidade: Mapped[int] = mapped_column(int)

  def __repr__(self):
    return f"Pedido(id={self.id!r}, produto={self.produto!r}, quantidade={self.quantidade!r})"