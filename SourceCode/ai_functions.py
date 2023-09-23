import os
import sys
import openai

from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")


# completion mode -> responde a la pregunta. Es el menos potente. No sigue un chat
# completion = openai.Completion.create(model="davinci-002", prompt=prompt)
# print(completion.choices[0].text)


def write_conversation_txt(chat_id: int, messages: str) -> bool:
    # Carpeta donde deseas guardar el archivo
    folder = 'conversations'
    # Si la carpeta no existe, créala
    if not os.path.exists(folder):
        os.makedirs(folder)
    # TEXTO PLANO
    archivo = os.path.join(folder, f'{chat_id}.txt')

    with open(archivo, 'w') as file: # w -> escritura. Reemplaza todo lo antiguo por lo nuevo
        # Escribe datos en el archivo
        file.write(str(messages))

    # with open(archivo, 'a+') as file: # a+ -> escritura. Añade a lo anterior, el mas significa (lectura y escritura)
    #     # Escribe datos en el archivo
    #     file.write("Hola, este es un ejemplo de escritura en un archivo de texto.\n")
    #     # file.write("Puedes agregar más líneas aquí si lo deseas.")
    return True

def read_conversation_txt(chat_id: int) -> list:
    folder = 'conversations'
    archivo = os.path.join(folder, f'{chat_id}.txt')
    with open(archivo, 'r') as file:
        messages = file.read()
    return messages



def __prompt() -> str: # si pones doble _ indica que la funcion es privada
	content = input("pregunta? :")
	if content == "exit":
		raise sys.exit()
	else:
		return content





# contexto del asistente -> contexto inicial
context = [{"role": "system",
             "content": "Eres un asistente muy util de programacion"}] # condicional del chat

messages = context

while True:

	content = __prompt()
	
	if content == "new":
		messages = context
		content = __prompt()

	# guardamos la preguas del usuario -> contexto de preguntas
	messages.append({"role": "user", "content": content})

	response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

	response_content = response.choices[0].message.content

	# guardamos la respuestas de chatgpt -> contexto de respuestaS
	messages.append({"role": "assistant", "content": response_content})
	print(messages)
	print(f"> {response_content}")