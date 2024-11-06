from fastapi import FastAPI

app = FastAPI()


@app.get('/')  # raiz no final do HTPP
def read_root():
    return {'message': 'Olá Mundo'}
