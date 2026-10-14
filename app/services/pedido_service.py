from typing import Sequence
from app.models.pedido import Pedido
from app.repositories.pedido_repository import PedidoRepository
from app.schemas.pedido import PedidoCreate


class PedidoService:
  def __init__(self, pedido_repository: PedidoRepository):
    self._pedido_repository = pedido_repository

  def listar_todos_os_pedidos(self) -> Sequence[Pedido]:
    return self._pedido_repository.list_all()

  def recuperar_pedido_via_id(self, pedido_id: int) -> Pedido | None:
    return self._pedido_repository.get(pedido_id)

  def adicionar_pedido(self, pedido: PedidoCreate) -> Pedido:
    novo_pedido = Pedido(
      produto=pedido.produto,
      quantidade=pedido.quantidade
    )

    return self._pedido_repository.add(novo_pedido)

  def deleta_pedido(self, pedido_id: int) -> None:
    return self._pedido_repository.delete(pedido_id)