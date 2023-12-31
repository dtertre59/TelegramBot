
from telegram import Update
from telegram.ext import ContextTypes
from telegram import InlineQueryResultArticle, InputTextMessageContent

import helper_functions, ai_functions, audio_functions

# ---------- MESSAGES FUNCTIONS ---------------------------------------------------------------------------------------------- #

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def m_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id=update.effective_chat.id
    audio_functions.url_download_audio(update)
    # descarga del audio en carpeta /audio2/audio.ogg
    # pasar a formato WAV
    audio_functions.audio_ogg_to_wav(f"audio_t/{chat_id}.ogg")
    # pasar de .wav a text
    question = audio_functions.audio_wav_to_text(f"audio_t/{chat_id}.wav", True)
    # enviar pregunta a chatgpt
    type, answer = ai_functions.message_menu(chat_id, question)
    if type == 't': # text
        await context.bot.send_message(chat_id, answer)
    elif type == 'a': # audio
        audio_path = audio_functions.text_to_audio_ogg(chat_id, answer)
        await context.bot.send_audio(chat_id=chat_id, audio=audio_path)

async def ia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id=update.effective_chat.id
    question = update.message.text
    type, answer = ai_functions.message_menu(chat_id, question)
    if type == 't': # text
        await context.bot.send_message(chat_id, answer)
    elif type == 'a': # audio
        audio_path = audio_functions.text_to_audio_ogg(chat_id, answer)
        await context.bot.send_audio(chat_id=chat_id, audio=audio_path)


# ---------- COMMANDS FUNCTIONS ---------------------------------------------------------------------------------------------- #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm an Ingenuity bot, please talk to me!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response_message = """
Hello! I'm Tunoo. Estas son las opciones disponibles:

COMMANDS:
/start - Iniciar la conversación
/help - Mostrar comandos
/d6 - Numero rand(1-6)
/animated_d6 - Animacion dado rand(1-6)
/flag country - foto de la bandera pais introducido
/audio - audio.mp3

PLAIN TEXT:
new -> new openai conversation

AUDIO:

"""
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response_message) #, parse_mode='html') # parac poder utilizar etiquetas HTML

# numero random del 1-6
async def d6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = helper_functions.roll_d6()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)

# gif de dado entre 1-6
async def animated_d6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = helper_functions.roll_d6()
    animation = helper_functions.get_d6_img(result)
    await context.bot.send_animation(chat_id=update.effective_chat.id,animation=animation)

# foto de la bandera dependiendo de la entrada del primer argumento
async def flag(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = helper_functions.get_url_flag(context.args[0])
    except:
        url = helper_functions.get_url_flag('ES')
    chat_id = update.message.chat_id
    await context.bot.send_photo(chat_id,url)

async def audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id=update.effective_chat.id
    text = " ".join(context.args)
    print(text)
    # audio_path = audio_functions.text_to_audio(chat_id, text)
    audio_path = audio_functions.text_to_audio_ogg(chat_id, text)
    await context.bot.send_audio(chat_id=chat_id, audio=audio_path)

# comando incorrecto
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


# ---------- INLINE FUNCTIONS ------------------------------------------------------------ #

async def inline_mayus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    print(query)
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='ALL Mayus',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)

async def inline_minus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    print(query)
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='ALL Minus',
            input_message_content=InputTextMessageContent(query.lower())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)






# -------- PRUEBAS -------------------------------------------------------- #


# async def pruebas(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     try:
#         msg = ' '.join(context.args).upper() # hace estring y lo pone en mayusculas
#         # msg = context.args[0]
#     except:
#         try:
#             msg = context.args[0] + " Provide 1 more arguments"
#         except:
#             msg = "Provide 2 more arguments"
#     chat_id = update.message.chat_id
#     await context.bot.send_message(chat_id,msg)
