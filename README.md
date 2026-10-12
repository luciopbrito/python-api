# python api

## 📌 Table of Contents

- [About](#-about)
- [Virtual environment — .venv](#virtual-environment--venv)
- [Activate the `.venv`](#activate-the-venv)
- [Concepts](#concepts) 
    - [How to import from package](#how-to-import-from-package)
    - [`__init__.py`](#__init__py) 
    - [project structure folder](#project-structure-folder)
    - [type annotation](#type-annotation)
- [FastAPI](#fastapi)
    - [Installing the FastAPI](#installing-the-fastapi)
    - [Using FastAPI class](#using-fastapi-class)
    - [Initializing the Web API](#initializing-the-web-api)
    - [Acessing the Web API documentation](#acessing-the-web-api-documentation) 
    - [APIRouter](#apirouter)
    - [Including router (APIRouter class) in FastAPI](#including-router-apirouter-class-in-fastapi)
    - [Depends function](#depends-function)
- [pydantic](#pydantic)
    - [BaseModel](#basemodel)
    - [Field](#field)
- [typing](#typing)
    - [Annotated](#annotated)

---

## 📖 About

The project goal is to understand the Python environment and define a Web API

---

## Virtual environment — .venv

It is crucial to set up a virtual environment to run the Python. The command to create a `.venv` folder quickly is below.

```sh
python -m venv .venv
```

## Activate the `.venv`

As we know, it is necessary to set up the `.venv` folder. After that, we need to enable the virtual environment. Run the
command below to activate the virtual environment on the current shell `.venv`.

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

For Python, this file is used to indicate that its folders is a module. In other words, the Python complier runs this file automatically. So, you can import whatever you want there, and the Python will handle them.

### project structure folder

The project structure folder will follow the example below.

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

It is common to define a specific type for a method or property. Python provides the optional type annotation. The code snippet below shows how to use it.

```python
def obter_pedido_service() -> PedidoService:
    return PedidoService()
```

## FastAPI

### Installing the FastAPI

To use the FastAPI package, we need to install first. The command to install it is below.

```sh
python -m pip install "fastapi[standard]"
```

### Using FastAPI class

After installing the `fastapi` package, it is necessary to import the `FastAPI` class.

```python
from fastapi import FastAPI
```

### Initializing the Web API

It is necessary to set up the Web API. The command to set up the Web API is below.

```sh
fastapi dev src/main.py
```

### Acessing the Web API documentation 

After initializing the Web API, you can access the documentation at the URL below. FastAPI also provides similar
documentation in OpenAPI format. It's good.

```txt
http://localhost:8080/docs
```

### APIRouter

It is a class from `fastapi` responsible for defining the controller (group of path operations — CRUD). As you can see below,  the `prefix` parameter defines the controller name.

```python
router = APIRouter(prefix="/pedidos", tags=["Pedidos"])
```

The code snippet below shows how to use the post path operation.

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

The `include_router` method is responsible for including the routers created from `APIRouter` class. The code snippet
below shows how to use it. 

```python
from fastapi import FastAPI
from app.api.routes import pedidos

app = FastAPI(title="API de Pedidos")

app.include_router(pedidos.router)
```

### Depends function

It is a function responsible for indicating the dependency. The code snippet below shows how to use it.

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

It is a Pydantic class with the responsibility of creating a Pydantic model. You can create the models easily.

### Field

It is a function from `pydantic` with the responsibility of creating a field with specific rule. The code snippet below 
defining a property as `string` with a rule that validates whether the string has at least 1 character.

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
    service: Annotated[
        PedidoService,
        Depends(PedidoService)
    ]
):
    return service.listar()
```
