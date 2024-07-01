from openai import OpenAI
from dotenv import load_dotenv
from time import sleep
from helpers import encodar_imagem
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4-vision-preview"

def analisar_imagem(caminho_imagem):
    prompt = """
        Assuma que você é um assitente de chatbot e que provavelmente o usuário está enviando a foto de um produto.
        Faça uma análise dele, e se for um produto com defeito, emita um parecer.
        Assuma que você sabe e processou uma imagem com Vision e a reposta será informada no formato de saída.

        # FORMATO DA RESPOSTA
        Minha análise para imagem consiste em: Parecer com indicativo de defeito ou desecrição do produto (se não houver defeito)

        ## Descreva a imagem
        Coloque a descrição aqui
    """

    imagem_base64 = encodar_imagem(caminho_imagem)

    resposta = cliente.chat.completions.create(
        model = modelo,
        messages = [
            {
                "role": "system", 
                "content": [
                    { 
                        "type": "text", 
                        "text": prompt 
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{imagem_base64}"
                        }
                    }
                ]
            }
        ],
        max_tokens = 300
    )

    return resposta.choices[0].message.content