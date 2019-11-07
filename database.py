import sqlite3

def sql_connection():
	con = sqlite3.connect('db.sqlite3')
	return con

def read_config():
	connection = sql_connection() 
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM plants_configuration")
	rows = cursor.fetchall()
	connection.close()
	return rows[0]