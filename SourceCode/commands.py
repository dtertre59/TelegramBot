
from telegram import Update
from telegram.ext import ContextTypes
from telegram import InlineQueryResultArticle, InputTextMessageContent

import helper_functions

# ---------- MESSAGES FUNCTIONS ---------------------------------------------------------------------------------------------- #

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def ia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id=update.effective_chat.id
    question = update.message.text
    answer = helper_functions.message_menu(chat_id, question)
    await context.bot.send_message(chat_id, answer)

# ---------- COMMANDS FUNCTIONS ---------------------------------------------------------------------------------------------- #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm an Ingenuity bot, please talk to me!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response_message = """
¡Hola! Soy el bot de Ingenuity. Estas son las opciones disponibles:
<b>/start</b> - Iniciar la conversación
<b>/help</b> - Mostrar comandos
<b>/d6</b> - Numero random entre 1 y 6
<b>/animated_d6</b> - Animacion de dado entre 1 y 6
<b>/flag country</b> - foto de la bandera del pais introducido
<b>/pruebas</b> - pruebas
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response_message, parse_mode='HTML') # parac poder utilizar etiquetas HTML

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


async def pruebas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        msg = ' '.join(context.args).upper() # hace estring y lo pone en mayusculas
        # msg = context.args[0]
    except:
        try:
            msg = context.args[0] + " Provide 1 more arguments"
        except:
            msg = "Provide 2 more arguments"
    chat_id = update.message.chat_id
    await context.bot.send_message(chat_id,msg)
