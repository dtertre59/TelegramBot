import os
import sys
import pickle
import openai

from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")


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
                "content": "Tu nombre es Aceituno, pero tus amigos te llaman Tuno. Cuando se inicia el chat nadie es tu amigo, ni yo, pero a medida que avanza la conversacion le coges cariño y ya nos convertimos en amigos.Eres mi amigo, por lo que tienes que responderme con la mayor veracidad a todas mis preguntas. Ya sabes como presentarte"}] # condicional del chat
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





# ---------- PRUEBAS Y FUNCIONES NO UTILIZADAS ------------------------------------------------ #

# completion mode -> responde a la pregunta. Es el menos potente. No sigue un chat
# completion = openai.Completion.create(model="davinci-002", prompt=prompt)
# print(completion.choices[0].text)


# def write_conversation_txt(chat_id: int, messages: str) -> bool:
#     # Carpeta donde deseas guardar el archivo
#     folder = 'conversations'
#     # Si la carpeta no existe, créala
#     if not os.path.exists(folder):
#         os.makedirs(folder)
#     # TEXTO PLANO
#     archivo = os.path.join(folder, f'{chat_id}.txt')

#     with open(archivo, 'w') as file: # w -> escritura. Reemplaza todo lo antiguo por lo nuevo
#         # Escribe datos en el archivo
#         file.write(str(messages))

#     # with open(archivo, 'a+') as file: # a+ -> escritura. Añade a lo anterior, el mas significa (lectura y escritura)
#     #     # Escribe datos en el archivo
#     #     file.write("Hola, este es un ejemplo de escritura en un archivo de texto.\n")
#     #     # file.write("Puedes agregar más líneas aquí si lo deseas.")
#     return True

# def read_conversation_txt(chat_id: int) -> list:
#     folder = 'conversations'
#     archivo = os.path.join(folder, f'{chat_id}.txt')
#     with open(archivo, 'r') as file:
#         messages = file.read()
#     return messages



# def __prompt() -> str: # si pones doble _ indica que la funcion es privada
# 	content = input("pregunta? :")
# 	if content == "exit":
# 		raise sys.exit()
# 	else:
# 		return content





# # contexto del asistente -> contexto inicial
# context = [{"role": "system",
#              "content": "Eres un asistente muy util de programacion"}] # condicional del chat

# messages = context

# while True:

# 	content = __prompt()
	
# 	if content == "new":
# 		messages = context
# 		content = __prompt()

# 	# guardamos la preguas del usuario -> contexto de preguntas
# 	messages.append({"role": "user", "content": content})

# 	response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

# 	response_content = response.choices[0].message.content

# 	# guardamos la respuestas de chatgpt -> contexto de respuestaS
# 	messages.append({"role": "assistant", "content": response_content})
# 	print(messages)
# 	print(f"> {response_content}")