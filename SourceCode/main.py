

from dotenv import load_dotenv
import os

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import commands



# Cargar las variables de entorno desde el archivo .env
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

print(TELEGRAM_BOT_TOKEN)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    start_handler = CommandHandler('start', commands.start)
    help_handler = CommandHandler('help', commands.help)  # Nuevo manejador para /help
    d6_handler = CommandHandler('d6', commands.d6)
    animated_d6_handler = CommandHandler('animated_d6', commands.animated_d6)
    flag_handler = CommandHandler('flag', commands.flag)
    pruebas_handler = CommandHandler('pruebas', commands.pruebas)

    application.add_handler(start_handler)
    application.add_handler(help_handler)  # Agrega el manejador de /help
    application.add_handler(d6_handler)
    application.add_handler(animated_d6_handler)
    application.add_handler(flag_handler)
    application.add_handler(pruebas_handler)
    
    
    application.run_polling()
