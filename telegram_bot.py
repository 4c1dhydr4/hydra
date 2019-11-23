#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import logging
import time
from blackhydra import Hydra
import database as db

hydra = Hydra('telegram')
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logs = []

main_menu = [
		[telegram.KeyboardButton('/status'), telegram.KeyboardButton('/send_cam_image')], 
		[telegram.KeyboardButton('/return_logs'), telegram.KeyboardButton('/hi')],
	]
kb_main_menu = telegram.ReplyKeyboardMarkup(main_menu)

TOKEN = hydra.config['telegram']['token']
my_chat_id = hydra.config['telegram']['chats_id'][0]

#Definición de Utilitarios
def get_user(update):
	first_name = update.message.from_user.first_name
	last_name = update.message.from_user.last_name
	first_name = str(first_name)
	last_name = str(last_name)
	user_text = first_name +  " " + last_name
	return user_text

def get_time():
	times = time.asctime(time.localtime(time.time()))
	return times

def put_log(log,update):
	user_text = get_user(update)
	hora = get_time()
	text = hora + "::" + log + " " + user_text
	global logs
	logs.append(text)
	return text

#Seguridad
def verify_log(bot, update):
	if(update.message.chat_id == my_chat_id):
		return True
	else:
		update.message.reply_text("No tienes permiso de hacer esto :(")
		send_message_to_me(bot, put_log("Permiso no concedido a: ",update))
		return False


#Retornos de Configuración

def get_move_config():
	return bot_config.return_move_alert()

def get_sound_config():
	return bot_config.return_sound_alert()

def get_humidity_config():
	return bot_config.return_humidity_alert()


#Definición de Menús
def start_menu(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Menú Principal", reply_markup=kb_main_menu)

"""
Definición de Envíos
"""
def send_message_to_me(bot, mensaje):
	bot.send_message(chat_id=my_chat_id, text=mensaje)

def send_cam_image(bot, update):
	if verify_log(bot, update):
		update.message.reply_text('Recibiendo datos...')
		ok, path = hydra.take_picture()
		if ok:
			bot.send_photo(chat_id=update.message.chat_id, photo=open(path, 'rb'))
		else:
			update.message.reply_text('Fallo al capturar fotografía')

def status(bot, update):
	sensors = db.get_last_sensor()
	text = "Sensores:\n Humedad: {}\nTemperatura: {}\nLuz: {}\nMovimiento: {}\nHumedad Ambiental:{}".format(
		sensors['H'], sensors['T'], sensors['L'], sensors['M'], sensors['A'])
	update.message.reply_text(text)
	send_message_to_me(bot, put_log("Datos de sensores enviados a",update))

def hi(bot, update):
	send_message_to_me(bot, put_log("Enviando frase a",update))
	text = hydra.hydra.get_random()
	update.message.reply_text(text)

def return_logs(bot, update):
	if verify_log(bot, update):
		mensaje = ""
		for data in logs:
			mensaje = mensaje + data + "\n"
		update.message.reply_text(mensaje)


#Menú Escencial

def start(bot, update):
	send_message_to_me(bot, put_log("Sesión iniciada por",update))
	update.message.reply_text('blackhydra_ en línea, Ingresa al menú principal: /start_menu')

def help(bot, update):
	update.message.reply_text('Si necesitas ayuda llama al 911')

def echo(bot, update):
	update.message.reply_text(update.message.text)

def error(bot, update, error):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, error)

def main():
	# time.sleep(20) #Para evitar que no se conecte
	"""Start the bot."""
	# Create the EventHandler and pass it your bot's token.
	hydra = Hydra('hydra')
	updater = Updater(TOKEN)


	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("hi", hi))
	dp.add_handler(CommandHandler("status", status))
	dp.add_handler(CommandHandler("start_menu", start_menu))
	dp.add_handler(CommandHandler("send_cam_image", send_cam_image))
	dp.add_handler(CommandHandler("return_logs", return_logs))
	dp.add_handler(CommandHandler("help", help))

	# on noncommand i.e message - echo the message on Telegram
	dp.add_handler(MessageHandler(Filters.text, echo))

	# log all errors
	dp.add_error_handler(error)

	# Start the Bot
	print("Iniciando Sesión en blackhydra_bot, Telegram")
	time.sleep(10)
	updater.start_polling()
	# Run the bot until you press Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	print("Sesión Iniciada")
	hydra.lcd_print('Telegram\nRunning')
	updater.idle()


if __name__ == '__main__':
	main()
