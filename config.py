config = {
	'active': True,
	'twitter':{
		'active': True,
		'api_token':'SFmdNrHuopjgqnFQxsZbcjtuS',
		'api_secret_key': 'tlHXnO4MGJsd4WAHUbt35h4U4NctekdhnR7Ot1FZ4Y1wasrQUF',
		'access_token': '954591665129508864-8E89CBbLS2dAZ8P5pcsEY3OB6KLTnBM',
		'access_token_secret': 'n4Hwd9tkXPqZRDmZLttoY4VGvrizT8rQ3SMaPLLcbEaAO',
	},
	'telegram':{
		'active': True,
		'token': '792970316:AAHzgtxfn-nyQYhNnraUSM0Uz7GEFrFRQJ0',
		'chats_id': (771607185,)
	},
	'instagram':{
		'active': True,
		'username': 'blackhydra__',
		'password': 'postgres',
	},
	'sensors':{
		'humidity':{ #Valores 
			'active': True,
			'bad': 500,
			'ok': 320,
			'good': 300,
			'much': 160,
			'twitter_post': [(10,30), (18,00)],
			'instagram_post': [(10,40), (18,10), (18,16)],
			'telegram_post': [(10,00), (18,20)],
		},
		'temperature':{ #C°
			'active': True,
			'bad': 15,
			'ok': 20,
			'good': 22,
			'much': 30,
			'twitter_post': [(10,35), (18,5)],
			'instagram_post': [(10,45), (18,15)],
			'telegram_post': [(10,5), (18,25)],
		},
		'light':{ #Horas luz
			'active': True,
			'bad': 8,
			'ok': 10,
			'good': 12,
			'much': 14,
			'twitter_post': [(6,35), (18,35)],
			'instagram_post': [(6,40), (18,40)],
			'telegram_post': [(6,45), (18,45)],
		},
		'movement':{ #Movimiento
			'active': True,
			'value': 700,
		},
		'ambient':{ # Humedad Ambiental
			'active': True,
			'bad': 70,
			'ok': 80,
			'good': 85,
			'much': 90,
			'twitter_post': [(6,35), (18,35)],
			'instagram_post': [(6,40), (18,40)],
			'telegram_post': [(6,45), (18,45)],
		},
	},
}

CATEGORY = {
	'bad': 1,
	'ok': 2,
	'good': 3,
	'much': 4,
	'alert': 5,
	'no_alert': 6,
}

def to_bool(value):
	bolean = True if value == 1 else False
	return bolean

def get_db_config(config, db_row):
	config['active'] = to_bool(db_row[1])
	config['twitter']['active'] = to_bool(db_row[8])
	config['telegram']['active'] = to_bool(db_row[7])
	config['instagram']['active'] = to_bool(db_row[6])
	config['sensors']['humidity']['active'] = to_bool(db_row[3])
	config['sensors']['temperature']['active'] = to_bool(db_row[9])
	config['sensors']['light']['active'] = to_bool(db_row[4])
	config['sensors']['movement']['active'] = to_bool(db_row[5])
	config['sensors']['ambient']['active'] = to_bool(db_row[2])
	return config