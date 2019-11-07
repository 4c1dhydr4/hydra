import time
from config import EVALUATION as ev

def ev_humidity(humidity_dic, sensor_value):
	if sensor_value >= humidity_dic['bad']:
		return ev['bad']
	elif sensor_value < humidity_dic['bad'] and sensor_value >= humidity_dic['ok']:
		return ev['ok']
	elif sensor_value < humidity_dic['ok'] and sensor_value >= humidity_dic['good']:
		return ev['good']
	elif sensor_value < humidity_dic['good'] and sensor_value >= humidity_dic['much']:
		return ev['much']
	elif sensor_value < humidity_dic['much']:
		return ev['much']
	else:
		return False

def ev_temperature(temperature_dic, sensor_value):
	if sensor_value <= temperature_dic['bad']:
		return ev['bad']
	elif sensor_value > temperature_dic['bad'] and sensor_value <= temperature_dic['ok']:
		return ev['ok']
	elif sensor_value > temperature_dic['ok'] and sensor_value <= temperature_dic['good']:
		return ev['good']
	elif sensor_value > temperature_dic['good'] and sensor_value <= temperature_dic['much']:
		return ev['much']
	elif sensor_value > temperature_dic['much']:
		return ev['much']
	else:
		return False

def ev_light(light_dic, sensor_value):
	if sensor_value <= light_dic['bad']:
		return ev['bad']
	elif sensor_value > light_dic['bad'] and sensor_value <= light_dic['ok']:
		return ev['ok']
	elif sensor_value > light_dic['ok'] and sensor_value <= light_dic['good']:
		return ev['good']
	elif sensor_value > light_dic['good'] and sensor_value <= light_dic['much']:
		return ev['much']
	elif sensor_value > light_dic['much']:
		return ev['much']
	else:
		return False

def ev_movement(movement_dic, sensor_value):
	if sensor_value <= movement_dic['value']:
		return ev['no_alert']
	elif sensor_value > movement_dic['value']:
		return ev['alert']
	else:
		return False

def ev_ambient(ambient_dic, sensor_value):
	if sensor_value <= ambient_dic['bad']:
		return ev['bad']
	elif sensor_value > ambient_dic['bad'] and sensor_value <= ambient_dic['ok']:
		return ev['ok']
	elif sensor_value > ambient_dic['ok'] and sensor_value <= ambient_dic['good']:
		return ev['good']
	elif sensor_value > ambient_dic['good'] and sensor_value <= ambient_dic['much']:
		return ev['much']
	elif sensor_value > ambient_dic['much']:
		return ev['much']
	else:
		return False

def post_humidity(humidity_dic, sensor_value):
	evaluation = ev_humidity(humidity_dic, sensor_value)
	#Aqui me quedé