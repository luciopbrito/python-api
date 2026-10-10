from fastapi import APIRouter

router = APIRouter(prefix="/heath")

@router.get(
  ""
)
def get_heath():
  return {"status": "OK"}