import time
from config import config, get_db_config
import arduino as r2d2
import database as db
from instapy_cli import client as instapy
import tweepy
import telegram
import logging
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from tools import *
import algorithm as hydra
import netifaces as ni
from lcd import lcd_print 

class Hydra:
	def __init__(self, name):
		self.name = name
		self.active = False
		self.port = False
		self.logs = []
		self.config = config
		self.tweepy = None
		self.telepy = None
		self.photo_id = 0
		self.db = db
		self.hydra = hydra

		self.initialize()

	def initialize(self):
		try:
			self.active = True
			self.tweepy = self.set_tweepy()
			self.telepy = self.set_telepy()
			self.set_config()
			self.port = r2d2.available_ports()[0]
		except Exception as e:
			self.manage_exception(e)

	def manage_exception(self, e):
		text = '({}) Error: {}'.format(timestamp(), str(e))
		self.add_log(text)
		self.send_text_to_me(text)
		lcd_print('Error Logged')
		
	def display_logs(self):
		for log in self.logs:
			print(log)

	def add_log(self, log):
		# self.logs.append(str(log))
		self.db.insert_log(str(log))

	def set_tweepy(self):
		auth = tweepy.OAuthHandler(
				self.config['twitter']['api_token'],
				self.config['twitter']['api_secret_key'])
		auth.set_access_token(
				self.config['twitter']['access_token'],
				self.config['twitter']['access_token_secret'])
		return tweepy.API(auth)

	def set_telepy(self):
		logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
		logger = logging.getLogger(__name__)
		return telegram.Bot(self.config['telegram']['token'])

	def read_serial(self):
		if self.port:
			return r2d2.get_sensors(self.port)
		else:
			self.manage_exception('No serial port available')
			return False, {'H': 1023, 'L': 6, 'M': 0, 'T': 20, 'A': 85}

	def take_picture(self):
		self.add_log("Trying to take a picture: {}".format(timestamp()))
		video_capture = cv2.VideoCapture(0)
		if not video_capture.isOpened():
			# raise Exception("Could not open video device")
			return False, None
		ret, frame = video_capture.read()
		video_capture.release()
		# im = Image.fromarray(crop_center(frame[:,:,::-1],350,350))
		im = Image.fromarray(frame[:,:,::-1])
		picture_name = "pictures/{}.png".format(self.photo_id)
		im.save(picture_name)
		self.photo_id += 1
		self.add_log("Picture {} taken: {}".format(self.photo_id, timestamp()))
		lcd_print('Picture Sended')
		return True, picture_name

	def post_instagram(self, text):
		self.add_log("Trying post on Instagram: {}".format(timestamp()))
		pic_ok, image = self.take_picture()
		if pic_ok:
			with instapy(self.config['instagram']['username'], self.config['instagram']['password']) as instagram:
				instagram.upload(image, text)
				self.add_log("Post on Instagram: {} - {}".format(text, timestamp()))
				lcd_print('Instagram Post')
		else:
			self.add_log("Taken picture error - {}".format(timestamp()))

	def post_twitter(self, text):
		try:
			self.add_log("Trying Posting on Twitter: {}".format(text))
			if len(text)<140:
				self.tweepy.update_status(text)
				self.add_log('Post on Twitter: {} - {}'.format(timestamp(), text))
				lcd_print('Twitter Post')
				return True
			else:
				print ("Text > 140 characters")
				return False
		except Exception as e:
			self.manage_exception('Twitter ' + str(e))

	def send_text_to_me(self, text):
		try:
			for chat_id in self.config['telegram']['chats_id']:
				self.add_log("Trying Sending Message to Chat #{}: {}".format(chat_id, text))
				self.telepy.send_message(chat_id=chat_id, text=text)
				self.add_log("Telegram message correctly sended to chat id #{}: {}".format(chat_id, text))
				lcd_print('Telegram Message')
		except Exception as e:
			self.manage_exception(e)

	def send_picture_to_me(self):
		ok, image_path = self.take_picture()
		if ok:
			try:
				for chat_id in self.config['telegram']['chats_id']:
					self.add_log("Trying Sending Photo to Chat #{}".format(chat_id))
					self.telepy.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
					self.add_log("Telegram photo correctly sended to chat id #{}".format(chat_id))
					lcd_print('Photo Sended')
			except Exception as e:
				self.manage_exception(e)
		else:
			self.add_log("Picture to Telegram error - {}".format(timestamp()))

	def get_ip(self):
		try:
			time.sleep(20)
			interface = ni.ifaddresses('wlan0')
			ip = interface[ni.AF_INET][0]['addr']
		except:
			ip = "192.168.1.-1"
		return ip

	def set_config(self):
		try:
			self.config = get_db_config(self.config, db.read_config())
			if self.config['active']:
				self.active = True
			else:
				self.active = False
		except Exception as e:
			self.manage_exception(e)

	def lcd_print(self, text):		
		lcd_print(text)

	def run(self):
		lcd_print('Initializing\nhydra')
		self.add_log("Initializing Hydra - {}".format(timestamp()))
		ip = 'Local IP:\n' + self.get_ip()
		self.db.insert_log(ip)
		lcd_print(ip)
		time.sleep(5)
		self.set_config()
		i = 0
		self.add_log("Running - {}".format(timestamp()))
		lcd_print('hydra running')
		while self.active:
			self.set_config()
			success, sensors = self.read_serial()
			if success:
				self.db.insert_sensors(sensors)
			self.hydra.post_humidity(self, sensors['H'])
			self.hydra.post_temperature(self, sensors['T'])
			self.hydra.post_light(self, sensors['L'])
			self.hydra.post_ambient(self, sensors['A'])
			self.hydra.movement_alert(self, sensors['M'])
			i += 1
			time.sleep(1)
		self.add_log("Kernel disabled - {}".format(timestamp()))






