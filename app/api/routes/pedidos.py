from fastapi import APIRouter, status
from app.schemas.pedido import PedidoCreate, PedidoResponse

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post(
    "",
    response_model=PedidoResponse,
    status_code=status.HTTP_201_CREATED,
)
def criar_pedido(pedido: PedidoCreate):
    return PedidoResponse(
        id=1,
        produto=pedido.produto,
        quantidade=pedido.quantidade,
        status="criado",
    )
