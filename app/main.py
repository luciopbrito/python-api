from fastapi import FastAPI
from app.api.routes import pedidos

app = FastAPI(title="python api")

app.include_router(pedidos.router)

@app.get("/health")
def health():
  return {"status": "ok"}