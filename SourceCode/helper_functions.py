
import random

import os
import ast
import pickle

import openai

from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")


def roll_d6() -> int:
    return random.randint(1,6)

def get_d6_img(n: int) -> str:
    # desde url
    # return f"https://github.com/bormolina/bormolina.github.io/blob/main/assets/d6_{n}_sd.webm"
    # desde local path
     image_path = f"images/d6_{n}_sd.gif"
     return image_path

def get_url_flag(country: str) -> str:
    url = f'https://flagsapi.com/{country}/flat/64.png'
    return url


# ---------- ARTIFICIAL INTELIGENT CHAT GPT -------------------------------------------------------------- #

def write_binary_conversation(chat_id: int, messages: str) -> bool:
    # Carpeta donde deseas guardar el archivo
    folder = 'conversations'
    # Si la carpeta no existe, créala
    if not os.path.exists(folder):
        os.makedirs(folder)
    # BINARIO
    # Ruta completa del archivo en la carpeta
    archivo = os.path.join(folder, f'{chat_id}.bin') # formqato archivo  binari
    # Abre el archivo en modo escritura binaria ('wb')
    with open(archivo, 'wb') as f:
        # Utiliza pickle para guardar el array en el archivo
        pickle.dump(messages, f)
    return True


def read_binary_conversation(chat_id: int):
    folder = 'conversations'
    archivo = os.path.join(folder, f'{chat_id}.bin')
    with open(archivo, 'rb') as file:
        binary_message = file.read()
    # Deserializar los datos binarios en un array (lista)
    message = pickle.loads(binary_message)
    return message



def new_conversation(chat_id: int):
    # contexto del asistente -> contexto inicial
    context = [{"role": "system",
                "content": "Eres un asistente muy util de programacion"}] # condicional del chat
    status = write_binary_conversation(chat_id, context)
    return status


def ai(chat_id: int, question: str) -> str:
    file = f'conversations/{chat_id}.bin'
    if not os.path.exists(file):    # si no existe el archivo lo creamos con la condicion inicial
        new_conversation(chat_id)
        print(f"creamos archivo: {file}")

    # cargamos los mensajes anteriores guardados en el txt especifico de cada chat de telegram para tener contexto de la conversacion
    messages = read_binary_conversation(chat_id)

    # guardamos la pregunta del usuario -> contexto de preguntas
    messages.append({"role": "user", "content": question})

    # respuesta de la ai
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    response_content = response.choices[0].message.content

	# guardamos la respuestas de chatgpt -> contexto de respuestas -> file.txt para que no se pierdaS
    messages.append({"role": "assistant", "content": response_content})
    write_binary_conversation(chat_id, messages)
    return response_content

# ---------- MAIN MESSAGE MENU --------------------------------------------------------------- #

def message_menu(chat_id: int, text: str) -> str:
    if text == "new":
        new_conversation(chat_id)
        return "new chatbot conversation 😈"
    elif text == "dtertre59":
        return "mi fooking padre"
    else:
        answer = ai(chat_id, text)
        return answer
