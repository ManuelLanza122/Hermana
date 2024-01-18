import telebot
import time
from flask import Flask
from threading import Thread
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token de las variables de entorno
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "¡El bot está en funcionamiento!"

@bot.message_handler(commands=['start'])
def enviar_felicitacion(message):
    chat_id = message.chat.id

    partes_mensaje = [
        "No tengo palabras para describir lo especial que eres para mí. ",
        "Sé que tu bandeja de entrada debe estar llena, porque eres una persona muy querida por todos. ",
        "Pero me gustaría recordarte todo el cariño que siento por ti y lo agradecido que estoy de tenerte en mi vida.\n\n",
        "Hoy, quiero desearte el más feliz de los cumpleaños. ",
        "Que este día esté lleno de celebración, abrazos apretados y sonrisas sinceras junto a las personas que más quieres. ",
        "Espero poder celebrar muchos años más contigo.\n\n",
        "¡Felicidades en tu día! 🎉"
    ]

    for parte in partes_mensaje:
        bot.send_message(chat_id, parte)
        time.sleep(2)  # Pausa de 2 segundos entre cada parte del mensaje

    # Añadir código para enviar fotos
    fotos_urls = ['https://telegra.ph/file/122c8910531724fcbebcf.jpg', 'https://telegra.ph/file/589f667db829128a7a2f4.jpg', 'https://telegra.ph/file/84251231b8beedda4ba8c.jpg']  # Agrega más URLs según sea necesario

    for foto_url in fotos_urls:
        msg = bot.send_photo(chat_id, foto_url)
        time.sleep(3)
        bot.delete_message(chat_id, msg.message_id)

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
bot.polling()
