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
		'password': '********',
	},
	'sensors':{
		'humidity':{ #Valores 
			'bad': 500,
			'ok': 320,
			'good': 300,
			'much': 160,
			'twitter_post': [(10,30), (18,00)],
			'instagram_post': [(10,40), (18,10)],
			'telegram_post': [(10,00), (18,20)],
		},
		'temperature':{ #C°
			'bad': 15,
			'ok': 20,
			'good': 22,
			'much': 26,
			'twitter_post': [(10,35), (18,5)],
			'instagram_post': [(10,45), (18,15)],
			'telegram_post': [(10,5), (18,25)],
		},
		'light':{ #Horas luz
			'bad': 8,
			'ok': 10,
			'good': 12,
			'much': 14,
			'twitter_post': [(6,35), (18,35)],
			'instagram_post': [(6,40), (18,40)],
			'telegram_post': [(6,45), (18,45)],
		},
	},
}