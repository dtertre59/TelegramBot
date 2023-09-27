# text to audio
from gtts import gTTS
# from pydub import AudioSegment
import pyttsx3

# audio to text
import speech_recognition as sr

import requests
import os
from dotenv import load_dotenv
# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Load your API key from an environment variable or secret management service

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_ACEITUNO_TOKEN')



def url_download_audio(update):
    voice_message = update.message.voice  # Obtener el mensaje de voz

    if voice_message:
        file_id = voice_message.file_id  # Obtener el file_id del mensaje de voz
        # Construir la URL de descarga del archivo de audio
        file_url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getFile?file_id={file_id}'
        print(file_url)
        # Realizar una solicitud GET para obtener la información del archivo
        response = requests.get(file_url)
        file_info = response.json()

        # Obtener el path del archivo descargado
        file_path = file_info['result']['file_path']

        # Construir la URL completa para descargar el archivo
        full_file_url = f'https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{file_path}'
        print(full_file_url)
        # Descargar el archivo de audio
        response = requests.get(full_file_url)
        
        if response.status_code == 200:
            # Guardar el archivo en tu sistema local
            with open('./audio2/audio.ogg', 'wb') as audio_file:
                audio_file.write(response.content)
                
            print('Archivo de audio descargado exitosamente.')
        else:
            print('Error al descargar el archivo de audio.')





def text_to_audio(chat_id: int, text: str) -> str:
    tts = gTTS(text=text, lang='es', slow= False)  # Puedes especificar el idioma, en este caso, español ('es')
    # audio = f"./audio/{chat_id}.mp3"
    audio = f"./audio/{chat_id}.wav"
    # Guardar el audio en un archivo MP3
    tts.save(audio)
    return audio


def text_to_audio_ogg(chat_id: int, text: str) -> str:
    engine = pyttsx3.init()
    # Control the rate. Higher rate = more speed
    engine.setProperty("rate", 150)
    output_file = f"./audio/{chat_id}.ogg"
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    return output_file


def audio_wav_to_text(filename:str) -> str:
    recognizer = sr.Recognizer()
    file_path = f"./audio2/{filename}.wav" # .wav only
    # open the file
    with sr.AudioFile(file_path) as source:
        try:
            print("Procesando...")
            # listen for the data (load audio to memory)
            audio_data = recognizer.record(source)
            # recognize (convert from speech to text)
            text = recognizer.recognize_google(audio_data, language='es-ES') # definir en que idimoa quieres reconocer la voz
            print(text)
            return text
        except sr.UnknownValueError:
            print("No se pudo reconocer el audio o no se detectó ninguna voz.")
        except sr.RequestError as e:
            print("Error en la solicitud: {0}".format(e))
        except FileNotFoundError:
            print("El archivo de audio no se encontró. Verifica la ruta y el nombre del archivo.")



def micro_to_text() -> str:
    recognizer = sr.Recognizer()
    # Configurar el micrófono (si tienes múltiples dispositivos, especifica el índice)
    mic = sr.Microphone(device_index=0)
    with mic as source:
        try:
            print("Escuchando...")
            # Escuchar durante un máximo de 10 segundos o hasta que se detecte silencio durante 2 segundos
            audio = recognizer.listen(source, timeout=100, phrase_time_limit=20)
            print("Procesando...")
            # Utilizar el motor de reconocimiento de voz de Google
            text = recognizer.recognize_google(audio, language='ES')
            print("Texto reconocido: " + text)
            return text
        except sr.UnknownValueError:
            print("No se pudo reconocer el audio")
        except sr.RequestError as e:
            print("Error en la solicitud: {0}".format(e))








# # Cargar el archivo MP3
# mp3_file = "audio.mp3"
# audio = AudioSegment.from_mp3(mp3_file)

# # Exportar el audio como OGG Vorbis
# ogg_file = "audio.ogg"
# # audio.export(ogg_file, format="ogg")



# engine = pyttsx3.init()
# # Control the rate. Higher rate = more speed
# engine.setProperty("rate", 150)
# text = "Hola mundo. Visita parzibyte.me"
# engine.say(text)
# """
# Queue another audio
# """
# another_text = "I like Python"
# engine.say(another_text)
# engine.runAndWait()


# audio = text_to_audio(1234, "hola que pasa")
# print(audio)
# text = "hola mundo"
# text_to_audio(text)

# from pydub import AudioSegment

# song = AudioSegment.from_mp3("never_gonna_give_you_up.mp3")

# song.export("mashup.mp3", format="mp3")
