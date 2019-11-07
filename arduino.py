import serial

def get_sensors(com):
	try:
		arduino = serial.Serial(com, 9600)
		line = arduino.readline()
		line = line.decode()
		line = line[0:len(line)-2]
		line = line.split("@")
		line.pop(0)
		sensors = {}
		for value in line:
			split = value.split(':')
			sensors[split[0]] = int(split[1])
		return True, sensors
	except:
		return False, {'H': 1023, 'L': 0, 'M': 0, 'T': 0, 'A': 0}

def available_ports():
	import sys
	from serial.tools import list_ports
	if sys.platform == 'win32':
		coms = [item.device for item in list_ports.comports()]
	elif sys.platform == 'linux2':
		coms = [item[0] for item in list_ports.comports()]
	return coms