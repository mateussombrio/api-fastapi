from fastapi import FastAPI
from fast_zero.schemas import Message
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', status_code=200, response_model=Message)
def read_root():

    return {'message': 'Olá mundo!'}


@app.get('/oi', status_code=200, response_class=HTMLResponse)
def ola_mundo():
    return """
    <html>
        <head>
            <title>Nosso óla </title>
        </head>
        <body>
            <h1> Olá Mundo </h1>
        </body>
    </html>"""
