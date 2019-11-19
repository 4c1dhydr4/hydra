import sqlite3
import random as r

phrases_categorys = {
	'temperature': 1,
	'humidity': 2,
	'light': 3,
	'mov': 4,
	'ambient': 2,
	'twitter': 7,
}

phrases_values = {
		'good':1,
		'much':2,
		'ok':3,
		'bad':5,
		'alert':7,
	}


def sql_connection(phrases=False):
	if phrases:
		con = sqlite3.connect('phrases.sqlite3')
	else:
		con = sqlite3.connect('db.sqlite3')
	return con

def read_config():
	connection = sql_connection() 
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM plants_configuration")
	rows = cursor.fetchall()
	connection.close()
	return rows[0]

def read_phrase(sensor, value):
	connection = sql_connection(True) 
	cursor = connection.cursor()
	cursor.execute(
		"SELECT * FROM neural_phrase WHERE category_id={} and value_id={}".format(
			phrases_categorys[sensor], phrases_values[value]
		))
	rows = cursor.fetchall()
	connection.close()
	return r.choice(rows)[1]