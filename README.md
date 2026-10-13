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

Notes: The file `__init__.py` does not necessarily need to have content in. However, whether you need to expose specific methods or property you can define them in `__init__.py`.

### project structure folder

The project structure folder will follow the example below.

```txt
python-api/
├── .venv/ # Virtual environment. 
├── app/ # Source code folder.
│   ├── __init__.py # Allow the app's folder to be a module. Could be considered the package API.
│   ├── main.py # Entrypoint of app module. (Initializing the Web API and its services).
│   ├── api/ # API content (routes, etc).
│   │   └── routes/ # Each controller (path operation) must be defined here.
│   │       └── pedidos.py # Represent controller (`/pedidos`). In other words, all endpoints that represent `pedido` resource.
│   ├── schemas/ # Each schema must be defined here.
│   │   └── pedido.py # Represent the `pedidos` schema.
│   ├── services/ # Each service must be defined here.
│   │   └── pedido_service.py # Represent the services that will be used to handle the business logic about `pedido` resource.
│   ├── repositories/ # Each repository must be defined here.
│   │   └── pedido_repository.py # Represent the repository that will be used to handle the `pedido` persistence. 
│   └── core/ # Each global configuration (e.g, configuration for external services, etc)
│       └── config.py # Represent Pydantic configuration.
├── tests/ # Suit for testing
├── pyproject.toml # File responsible for manage all packages in the project
└── README.md # Represent the documentation for the project.
```

### type annotation

It is common to define a specific type for a method or property. Python provides the optional type annotation. The code snippet below shows how to use it.

```python
def obter_pedido_service() -> PedidoService:
    return PedidoService()
```

### Handling packages

Every programming language has its own tools to handle packages. Some subjects will describe how to handle packages in 
Python below.

#### About `pyproject.toml`

It is a file responsible for tracking all packages to build the Python app. The important packages will be in
`[project].dependencies`. The development packages (e.g, packages that support the development period) will be in
`.[dev]`.

An example of `pyproject.toml` is below.

```toml
[project]
name = "python-api"
version = "0.0.0"
requires-python = ">=3.14.7"
dependencies = [
    "fastapi[standard]"
]

[project.optional-dependencies]
dev = ["pytest>=7.0", "ruff"]
```

#### how to install dependencies from `pyproject.toml` via pip

```bash
pip install -e .
```

**Notes: It is necessary to have a appropriate `pyproject.toml` with `[project].dependencies` property** 

#### how to set up the dependencies into requirements.txt via pip

Below, it has a command that prints all packages from `.venv` to `requirements.txt`

```bash
pip freeze > requirements.txt
```

#### how to install dependencies from requirements.txt via pip

To install dependencies from `requirements.txt` via `pip`, it is necessary to pass the `-r` parameter with a value
corresponding to the `requirements.txt` path.

```bash
pip install -r <requirements.txt-path>
```

### How to document a method or property

Python also supports the documentation for methods and properties. The follow code snippet describes how to implement it.

```python
class User:
  def greetings(self):
    """Function return the content 'hello' as string"""
    return self.greeting_message

  greeting_message = "Hello!!"
  """Variable with string value"""
```

## Poetry

Poetry is a dependency manager tracking local dependencies of your projects and libraries.

### Why do you must use the Poetry?

Poetry solves the problem of installing packages via pip. Make the changes to `pyproject.toml`.

### How to install package with poetry

```bash
poetry install sqlalchemy
```

### How to uninstall/remove package with poetry

```bash
poetry remove sqlalchemy
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

## SQLAlchemy

It is a package that handles the connection to the SQL databases.

### create_engine

It is a function that handles with SQL engine in Python. In other words, it defines pre-configuration that will be used in
the `sessionmaker` class.

```python
engine = create_engine(
  "mysql+mysqldb://scott:tiger@hostname/dbname",
  pool_pre_ping=True,
  pool_recycle=36000
)
```

### sessionmaker

It is a class responsible for setting up the session that Python will use to connect to the database. The `engine`
variable must return the result of `create_engine`.

```python
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
```