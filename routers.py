from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/converter")
def converter():
    return {"message": "Its work!"}
