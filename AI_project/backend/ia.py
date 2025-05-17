import os
from dotenv import load_dotenv
import openai

# Carrega as variáveis do .env
load_dotenv()

# Pega a chave da OpenAi do .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

def gerar_resposta(pergunta: str) -> str:
    """
    Chama a API do OpenAI para gerar uma resposta para a pergunta dada."""
    try:
        reponse = openai.ChatCompletion.create(
            model="gpt-3.5-turob",
            messages=[
                {"role": "system", "content": "Você é um assistente útil e educado."},
                {"role": "user", "content": pergunta},
            ],
            max_tokens=150,
            temperature=0.7,
            n=1,
        )
        resposta = response.choices[0].message.content.strip()
        return resposta
    
    except Excption as e:
        return f"Erro ao chamar a API: {e}"