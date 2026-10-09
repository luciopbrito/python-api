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
