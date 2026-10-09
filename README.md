# python api

The project goal is to handle with python environment, and define an Web API.

## Virtual environment — .venv

It is crucial to define a virtual environment to run the python. The command to create a `.venv` folder quickly is below.

```sh
python -m venv .venv
```

## enter in .venv

As we know, it is necessary to define the .venv folder. After that, we need to enter into virtual environment. Run the command below to enter into .venv

```sh
source .venv/bin/activate
```

## Concepts 

### How to import from package

The syntax is very similar with nodejs-way.

```python
from <package> import <definition/source>
```

### `__init__.py` 

For Python, this file is used to indicate that its folder is a module. In other words, the Python complier runs this file automaticly. So, you can import whatever you want there, and the Python will handle it.

### project struture folder

The project struture folder will follow the example below.

```txt
python-api/
├── .venv/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   └── routes/
│   │       └── pedidos.py
│   ├── schemas/
│   │   └── pedido.py
│   ├── services/
│   │   └── pedido_service.py
│   ├── repositories/
│   │   └── pedido_repository.py
│   └── core/
│       └── config.py
├── tests/
├── pyproject.toml
├── .env.example
└── README.md
```

### type annotation

It is common to define a specific type for a method or property. Python provides the optional type annotation. The snippet code below shows how to use it.

```python
def obter_pedido_service() -> PedidoService:
    return PedidoService()
```

## FastAPI

### Installing the FastAPI

To use the FastAPI package, we need to install first. The command to install is below.

```sh
python -m pip install "fastapi[standard]"
```

### Using FastAPI class

After installing the `fastapi` package. It is necessary to import class `FastAPI`.

```python
from fastapi import FastAPI
```

### Initializing the Web API

It is necessary to set up the Web API. The command to set up the Web API is below.

```sh
fastapi dev src/main.py
```

### Acessing the Web API documentation 

After initializing the Web API you can access the documentiation by URL below. The FastAPI has a simular documentation with OpenAPI-style. It's good.

```txt
http://localhost:8080/docs
```

### APIRouter

It is a class from `fastapi` responsible for defining the controller (group of path operations — CRUD). As you can see below,  the `prefix` parameter defines the controller name.

```python
router = APIRouter(prefix="/pedidos", tags=["Pedidos"])
```

The snippet code below shows how to use the post path operation.

```python
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
```

### Including router (APIRouter class) in FastAPI

The `include_router` method is to responsible for including the routers created from `APIRouter` class. The snippet code below shows how to use it.

```python
from fastapi import FastAPI
from app.api.routes import pedidos

app = FastAPI(title="API de Pedidos")

app.include_router(pedidos.router)
```

### Depends

It is a function responsible for indicating the dependency. The snippet code below shows how to use it.

```python
from fastapi import APIRouter, status, Depends
from app.schemas.pedido import PedidoCreate, PedidoResponse
from app.services.pedido_service import PedidoService
from typing import Annotated

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.get(
    "",
    response_model=list[PedidoResponse],
    status_code=status.HTTP_200_OK
)
def list_pedidos(
    service: Depends(PedidoService)
):
    return service.listar()
```

## pydantic

It is a common module from Python. Because of this, it is not necessary to install via `pip`. 

### BaseModel

It is a class from `pydantic` with responsibility of creating pydantic model. You can create the models easily.

### Field

It is a function from `pydantic` with responsibility of creating a field with specific rule. The snippet code below defining a property as `string` with a rule that validates whether the string has at least 1 character.

```python
produto: str = Field(min_length=1)
```

## typing

### Annotated

Annotated is a class from Python's typing module that allows metadata to be associated with a type annotation. In FastAPI, it can be used with Depends() to declare dependencies directly in a function's parameters.

The following example demonstrates how to use Annotated to inject a PedidoService instance into the list_pedidos endpoint without manually creating an instance inside the function.

FastAPI resolves the dependency and passes the resulting instance to the endpoint, keeping dependency management separate from the endpoint's business logic.

```python
from fastapi import APIRouter, status, Depends
from app.schemas.pedido import PedidoCreate, PedidoResponse
from app.services.pedido_service import PedidoService
from typing import Annotated

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.get(
    "",
    response_model=list[PedidoResponse],
    status_code=status.HTTP_200_OK
)
def list_pedidos(
   service: Depends(PedidoService)
):
    return service.listar()
```
