from fastapi import FastAPI
from http import HTTPStatus
from fast_zero.schemas import Message

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK)  # raiz no final do HTPP
def read_root():
    return {"message": "Olá Mundo"}