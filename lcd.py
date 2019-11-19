import sys
if sys.platform == 'win32':
	OS = 'win'
elif sys.platform == 'linux':
	OS = 'linux'
	import Adafruit_CharLCD as LCD
	import time
	lcd_rs = 25
	lcd_en = 24
	lcd_d4 = 23
	lcd_d5 = 17
	lcd_d6 = 18
	lcd_d7 = 22
	lcd_backlight = 4
	lcd_columns = 16
	lcd_rows = 2
	lcd = LCD.Adafruit_CharLCD(
		lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
		lcd_columns, lcd_rows, lcd_backlight)


def lcd_print(text):
	if OS == 'win':
		return print(text)
	elif OS == 'linux':
		# charts = len(text)
		lcd.clear()
		lcd.message(text)
		# if charts < 16:
		# 	lcd.message(text)
		# elif charts <32:
		# 	lcd.message(text)
		# 	for i in range(charts):
		# 		time.sleep(0.5)
		# 		lcd.move_left()
		# 	lcd.clear()
