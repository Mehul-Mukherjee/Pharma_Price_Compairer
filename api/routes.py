from fastapi import APIRouter

router = APIRouter()

@router.get("/search")
def search(q: str):
    return {"query": q, "result": "implement service call here"}