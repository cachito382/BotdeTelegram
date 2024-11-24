#Para ejecutar el archivo , en linea de comando escribir "python main.py"

import telebot
import serial,time

#Conexion con el puerto (?)

arduino = serial.Serial('COM3',9600)
time.sleep(2)

#Conexion con nuestro bot

TOKEN = '7973323183:AAFAW-ZcriAk3hvjX_-M_eodurhr6hbKs5Y'
bot = telebot.TeleBot(TOKEN)

#Creacion de Comandos

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Saludos! , Soy el Bot de Telegram Mr.GreenApples , si estas leyendo este mensaje estoy funcionando correctamente :D . \nPara ver mis funciones haz uso del comando \n/help')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,'Para interactuar conmigo haz uso de los comandos /encender o /apagar , ante cualquier otro mensaje no sere capaz de proporcionarte alguna respuesta')

@bot.message_handler(commands=['encender'])
def send_encender(message):
    arduino.write(b'1')
    
    bot.reply_to(message,'El Led esta encendido !')

@bot.message_handler(commands=['apagar'])
def send_apagar(message):
    arduino.write(b'A')
    
    bot.reply_to(message,'El Led esta apagado !')

@bot.message_handler(func=lambda m:True)
def echo_all(message):
    bot.reply_to(message,'Lo siento no soy capaz de responder ante cualquier mensaje , para mas ayuda utiliza el comando /help')

if __name__ == "__main__":
    bot.polling(none_stop=True)