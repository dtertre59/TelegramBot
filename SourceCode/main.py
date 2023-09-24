

from dotenv import load_dotenv
import os

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, InlineQueryHandler

import commands


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_ACEITUNO_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    print("INICIANDO BOT")
    
    # Command handler --> /command anyth
    start_handler = CommandHandler('start', commands.start)
    help_handler = CommandHandler('help', commands.help)  # Nuevo manejador para /help
    d6_handler = CommandHandler('d6', commands.d6)
    animated_d6_handler = CommandHandler('animated_d6', commands.animated_d6)
    flag_handler = CommandHandler('flag', commands.flag)
    audio_handler = CommandHandler('audio', commands.audio)
    
    pruebas_handler = CommandHandler('pruebas', commands.pruebas)

    # Message handler --> text
    # echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), commands.echo) # no deja pasar los comandos -> condicion en el filtro
    ia_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), commands.ia)
    unknown_handler = MessageHandler(filters.COMMAND, commands.unknown)

    # inline handler --> @bot query
    inline_mayus_handler = InlineQueryHandler(commands.inline_mayus) # solo funciona la rimera que se pone. es como si estubiera limitado a una inline unicamente
    inline_minus_handler = InlineQueryHandler(commands.inline_minus)
    

    # add
    application.add_handler(start_handler)
    application.add_handler(help_handler)  # Agrega el manejador de /help
    application.add_handler(d6_handler)
    application.add_handler(animated_d6_handler)
    application.add_handler(flag_handler)
    application.add_handler(audio_handler)

    application.add_handler(pruebas_handler)

    # application.add_handler(echo_handler)
    application.add_handler(ia_handler)
    application.add_handler(unknown_handler)

    application.add_handler(inline_minus_handler)
    application.add_handler(inline_mayus_handler)
    
    
    # RUN
    application.run_polling()
