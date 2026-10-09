from fastapi import FastAPI

app = FastAPI(title="python api")

@app.get("/health")
def health():
  return {"status": "ok"}