from fastapi import FastAPI
from app.api.routes import pedidos, health

app = FastAPI(title="python api")

app.include_router(pedidos.router)
app.include_router(health.router)