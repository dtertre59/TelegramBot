from gtts import gTTS
# from pydub import AudioSegment

import pyttsx3


def text_to_audio(chat_id: int, text: str) -> str:
    tts = gTTS(text=text, lang='es', slow= False)  # Puedes especificar el idioma, en este caso, español ('es')
    audio = f"./audio/{chat_id}.mp3"
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
