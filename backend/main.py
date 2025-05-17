from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatgpt import gerar_resposta

app = FastAPI()

class Pergunta(BaseModel):
    pergunta: str

@app.post("/chat")
async def chat_endpoint(item: Pergunta):
 reposta = gerar_respota(item.pergunta)
 if reposta.startswith("Erro"):
        raise HTTPException(status_code=500, detail=gerara_resposta)
 return {"resposta": resposta}