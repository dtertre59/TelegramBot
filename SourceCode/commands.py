
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import functions

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm an Ingenuity bot, please talk to me!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response_message = """¡Hola! Soy el bot de Ingenuity. Estas son las opciones disponibles:
    /start - Iniciar la conversación
    /help - Mostrar comandos
    /d6 - Numero random entre 1 y 6
    /animated_d6 - Animacion de dado entre 1 y 6
    /flag country - foto de la bandera del pais introducido
    /pruebas - pruebas
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response_message)

# numero random del 1-6
async def d6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = functions.roll_d6()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)

# gif de dado entre 1-6
async def animated_d6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = functions.roll_d6()
    animation = functions.get_d6_img(result)
    await context.bot.send_animation(chat_id=update.effective_chat.id,animation=animation)

# foto de la bandera dependiendo de la entrada del primer argumento
async def flag(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = functions.get_url_flag(context.args[0])
    except:
        url = functions.get_url_flag('ES')
    chat_id = update.message.chat_id
    await context.bot.send_photo(chat_id,url)


async def pruebas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        msg = context.args[1]
    except:
        try:
            msg = context.args[0] + " Provide 1 more arguments"
        except:
            msg = "Provide 2 more arguments"
    chat_id = update.message.chat_id
    await context.bot.send_message(chat_id,msg)
