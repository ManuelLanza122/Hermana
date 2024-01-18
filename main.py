import telebot
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token de las variables de entorno
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def enviar_felicitacion(message):
    chat_id = message.chat.id

    mensaje_cumpleanos = (
        "¡Feliz cumpleaños! 🎉🎂\n\n"
        "Espero que tengas un día lleno de alegría y momentos especiales. "
        "Que cada momento esté rodeado de las personas que más quieres. ¡Disfruta al máximo tu día Te amo hermanita bella!"
    )

    bot.send_message(chat_id, mensaje_cumpleanos)

    # Añadir código para enviar una sola foto
    foto_url = 'https://telegra.ph/file/122c8910531724fcbebcf.jpg'
    bot.send_photo(chat_id, foto_url)

# Iniciar el bot
bot.polling()
