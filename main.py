from fastapi import FastAPI
from routers import router

app = FastAPI()
app.include_router(router=router)


@app.get("/")
def read_root():
    return {"message": "Olá Mundo!"}
