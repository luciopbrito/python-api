from pydantic import BaseModel, Field

class PedidoCreate(BaseModel):
    produto: str = Field(min_length=1)
    quantidade: int = Field(gt=0)

class PedidoResponse(BaseModel):
    id: int
    produto: str
    quantidade: int
    status: str
