import time
from datetime import datetime
from config import CATEGORY
from database import read_phrase
from lcd import lcd_print 

def ev_humidity(humidity_dic, sensor_value):
	if sensor_value >= humidity_dic['bad']:
		return CATEGORY['bad']
	elif sensor_value < humidity_dic['bad'] and sensor_value >= humidity_dic['ok']:
		return CATEGORY['ok']
	elif sensor_value < humidity_dic['ok'] and sensor_value >= humidity_dic['good']:
		return CATEGORY['good']
	elif sensor_value < humidity_dic['good'] and sensor_value >= humidity_dic['much']:
		return CATEGORY['much']
	elif sensor_value < humidity_dic['much']:
		return CATEGORY['much']
	else:
		return False

def ev_temperature(temperature_dic, sensor_value):
	if sensor_value <= temperature_dic['bad']:
		return CATEGORY['bad']
	elif sensor_value > temperature_dic['bad'] and sensor_value <= temperature_dic['ok']:
		return CATEGORY['ok']
	elif sensor_value > temperature_dic['ok'] and sensor_value <= temperature_dic['good']:
		return CATEGORY['good']
	elif sensor_value > temperature_dic['good'] and sensor_value <= temperature_dic['much']:
		return CATEGORY['much']
	elif sensor_value > temperature_dic['much']:
		return CATEGORY['much']
	else:
		return False

def ev_light(light_dic, sensor_value):
	if sensor_value <= light_dic['bad']:
		return CATEGORY['bad']
	elif sensor_value > light_dic['bad'] and sensor_value <= light_dic['ok']:
		return CATEGORY['ok']
	elif sensor_value > light_dic['ok'] and sensor_value <= light_dic['good']:
		return CATEGORY['good']
	elif sensor_value > light_dic['good'] and sensor_value <= light_dic['much']:
		return CATEGORY['much']
	elif sensor_value > light_dic['much']:
		return CATEGORY['much']
	else:
		return False

def ev_movement(movement_dic, sensor_value):
	if sensor_value > movement_dic['value']:
		return CATEGORY['alert']
	else:
		return False

def ev_ambient(ambient_dic, sensor_value):
	if sensor_value <= ambient_dic['bad']:
		return CATEGORY['bad']
	elif sensor_value > ambient_dic['bad'] and sensor_value <= ambient_dic['ok']:
		return CATEGORY['ok']
	elif sensor_value > ambient_dic['ok'] and sensor_value <= ambient_dic['good']:
		return CATEGORY['good']
	elif sensor_value > ambient_dic['good'] and sensor_value <= ambient_dic['much']:
		return CATEGORY['much']
	elif sensor_value > ambient_dic['much']:
		return CATEGORY['much']
	else:
		return False

def ev_hours(hours):
	now = datetime.now()
	for hour in hours:
		if hour[0] == now.hour and hour[1] == now.minute:
			return True
	return False

def get_phrase(category, sensor):
	# Implementar toma de frases desde db
	if category == 1:
		return read_phrase(sensor, 'bad')
		# return 'Niveles Bajos de {} - {}'.format(text, sensor)
	if category == 2:
		return read_phrase(sensor, 'ok')
		# return 'Niveles Neutros de {} - {}'.format(text, sensor)
	if category == 3:
		return read_phrase(sensor, 'good')
		# return 'Niveles Buenos de {} - {}'.format(text, sensor)
	if category == 4:
		return read_phrase(sensor, 'much')
		# return 'Exceso de {} - {}'.format(text, sensor)
	if category == 5:
		return read_phrase(sensor, 'alert')
		# return 'Alerta de {} - {}'.format(text, sensor)
	if category == 7:
		return read_phrase('twitter', 'ok')
	else:
		return 'Problemas en el Kernel de Hydra'


def ev(hydra, sensor, category, sensor_value):
	if hydra.config['sensors'][sensor]['active']:
		if hydra.config['twitter']['active']:
			if ev_hours(hydra.config['sensors'][sensor]['twitter_post']):
				hydra.post_twitter(get_phrase(category, sensor))
				print('Sleeping for 60 seconds')
				time.sleep(60)
		if hydra.config['telegram']['active']:
			if ev_hours(hydra.config['sensors'][sensor]['telegram_post']):
				hydra.send_text_to_me(get_phrase(category, sensor))
				print('Sleeping for 60 seconds')
				time.sleep(60)
		if hydra.config['instagram']['active']:
			if ev_hours(hydra.config['sensors'][sensor]['instagram_post']):
				hydra.send_picture_to_me()
				print('Sleeping for 60 seconds')
				time.sleep(60)

def post_humidity(hydra, sensor_value):
	ev(hydra, 'humidity', ev_humidity(hydra.config['sensors']['humidity'], sensor_value), sensor_value)

def post_temperature(hydra, sensor_value):
	ev(hydra, 'temperature', ev_temperature(hydra.config['sensors']['temperature'], sensor_value),sensor_value)

def post_light(hydra, sensor_value):
	ev(hydra, 'light', ev_light(hydra.config['sensors']['light'], sensor_value),sensor_value)

def post_ambient(hydra, sensor_value):
	ev(hydra, 'ambient', ev_ambient(hydra.config['sensors']['ambient'], sensor_value),sensor_value)

def movement_alert(hydra, sensor_value):
	move_config = hydra.config['sensors']['movement']
	category = ev_movement(move_config, sensor_value)
	if category == 5 and move_config['active']:
		lcd_print('Movement alert\nactive')
		time.sleep(2)
		if hydra.config['telegram']['active']:
			hydra.send_text_to_me(get_phrase(category, 'mov'))
			hydra.send_picture_to_me()
		if hydra.config['twitter']['active']:
			hydra.post_twitter(get_phrase(category, 'mov'))
		print('Sleeping for 5 seconds')
		time.sleep(5)

import random
def get_random():
	return get_phrase(7, 'ok')


