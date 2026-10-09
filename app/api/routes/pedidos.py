from fastapi import APIRouter, status, Depends
from app.schemas.pedido import PedidoCreate, PedidoResponse
from app.services.pedido_service import PedidoService
from typing import Annotated

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

@router.get(
    "",
    response_model=list[PedidoResponse],
    status_code=status.HTTP_200_OK
)
def list_pedidos(
    service: Annotated[
        PedidoService,
        Depends(PedidoService)
    ]
):
    return service.listar()