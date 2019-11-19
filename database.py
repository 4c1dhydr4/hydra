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

def open_db(phrases=False):
	if phrases:
		con = sqlite3.connect('phrases.sqlite3')
	else:
		con = sqlite3.connect('db.sqlite3')
	c = con.cursor()
	return con, c

def close_db(conn, c):
	c.close()
	conn.close()

def read_config():
	connection, cursor = open_db() 
	cursor.execute("SELECT * FROM plants_configuration")
	rows = cursor.fetchall()
	close_db(connection, cursor)
	return rows[0]

def insert_sensors(val):
	connection, cursor = open_db()
	sql = "INSERT INTO plants_sensorvalue(temperature, humidity, light, mov, ambient) VALUES(?,?,?,?,?)"
	task = (val['T'], val['H'], val['L'], val['M'], val['A'])
	cursor.execute(sql, task)
	connection.commit()
	rows = cursor.fetchall()
	close_db(connection, cursor)

def insert_log(log):
	connection, cursor = open_db()
	sql = "INSERT INTO plants_log(log) VALUES(?)"
	cursor.execute(sql,(log,))
	connection.commit()
	rows = cursor.fetchall()
	close_db(connection, cursor)	

def get_last_sensor():
	connection, cursor = open_db()
	cursor.execute("SELECT * FROM plants_sensorvalue WHERE id=(SELECT MAX(id) FROM plants_sensorvalue);")
	row = cursor.fetchall()[0]
	close_db(connection, cursor)
	sensor = {
		'T':row[1],
		'H':row[2],
		'L':row[3],
		'M':row[4],
		'A':row[5],
	}
	return sensor

def read_phrase(sensor, value):
	connection, cursor = open_db(True) 
	cursor.execute(
		"SELECT * FROM neural_phrase WHERE category_id={} and value_id={}".format(
			phrases_categorys[sensor], phrases_values[value]
		))
	rows = cursor.fetchall()
	close_db(connection, cursor)
	return r.choice(rows)[1]