from fastapi import APIRouter

router = APIRouter()


@router.post("/users/", tags=["users"])
async def root():
    return [{"username": "Rick"}, {"username": "Morty"}]
