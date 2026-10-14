from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.database import get_session
from app.repositories.pedido_repository import PedidoRepository
from app.schemas.pedido import PedidoCreate, PedidoResponse
from app.services.pedido_service import PedidoService
from typing import Annotated

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

def get_pedido_service(session: Session = Depends(get_session)) -> PedidoService:
    repository = PedidoRepository(session)
    return PedidoService(repository)

@router.post(
    "",
    response_model=PedidoResponse,
    status_code=status.HTTP_201_CREATED,
)
def criar_pedido(
    pedido: PedidoCreate,
    pedido_service: Annotated[
        PedidoService,
        Depends(get_pedido_service)
    ]
):
    pedido_response = pedido_service.adicionar_pedido(pedido)
    
    return PedidoResponse(
        id=pedido_response.id,
        produto=pedido_response.produto,
        quantidade=pedido_response.quantidade,
        status=pedido_response.status,
    )

@router.get(
    "",
    response_model=list[PedidoResponse],
    status_code=status.HTTP_200_OK
)
def list_pedidos(
    pedido_service: Annotated[
        PedidoService,
        Depends(get_pedido_service)
    ]
):
    return pedido_service.listar()

@router.get(
    "/{pedido_id}",
    response_class=PedidoResponse,
    status_code=status.HTTP_200_OK
)
def recupera_pedido_via_id(
    pedido_id: int,
    pedido_service: Annotated[
        PedidoService,
        Depends(get_pedido_service)
    ]
):
    return pedido_service.recuperar_pedido_via_id(pedido_id=pedido_id)