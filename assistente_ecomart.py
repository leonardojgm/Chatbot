from openai import OpenAI
from dotenv import load_dotenv
from time import sleep
from helpers import *
from selecionar_persona import *
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"
contexto = carrega("dados/ecomart.txt")

def criar_thread():
    return cliente.beta.threads.create()

def criar_assistente():
    assistente = cliente.beta.assistants.create(
        name = "Atendente EcoMart",
        instructions = f"""
            Você é um chatbot de atendimento a clientes de um e-commerce.
            Você não deve reponder perguntas que não seja dados do e-commerce informado!
            Além disso, adote a persona abaixo para responder ao cliente.

            ## Contexto
            {contexto}

            ## Persona
            {personas["neutro"]}
        """,
        model = modelo
    )

    return assistente