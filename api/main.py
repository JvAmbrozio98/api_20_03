from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class InfoPrevisao(BaseModel):
    empresa : str
    volume : float
    prev_fecham : float


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/previsoes")
def previsoes(infoPrevisao : InfoPrevisao):

    if infoPrevisao.empresa == "aapl":
        w0, w1, w2 = [-15.364324084645187, 1.0639578280039346, -3.2354336426203774e-09]
        previsao = w0 + w1 * infoPrevisao.prev_fecham + w2 * infoPrevisao.volume
    else:
        previsao = None

    return { "profecia" : previsao }