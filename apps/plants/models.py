from django.db import models

class Configuration(models.Model):
	active = models.BooleanField(
		help_text="Activar o Desactivar Hydra",
		verbose_name="Activo")
	post_twitter = models.BooleanField(
		default = True,
		help_text="Comunicación con Twitter",
		verbose_name="Comunicación con Twitter")
	post_telegram = models.BooleanField(
		default = True,
		help_text="Comunicación con Telegram",
		verbose_name="Comunicación con Telegram")
	post_instagram = models.BooleanField(
		default = True,
		help_text="Comunicación con Instagram",
		verbose_name="Comunicación con Instagram")
	movement_alert = models.BooleanField(
		default = True,
		help_text="Alerta de Movimiento",
		verbose_name="Alerta de Movimiento")
	humidity_alert = models.BooleanField(
		default = True,
		help_text="Alerta de Humedad",
		verbose_name="Alerta de Humedad")
	temperature_alert = models.BooleanField(
		default = True,
		help_text="Alerta de Temperatura",
		verbose_name="Alerta de Temperatura")
	light_alert = models.BooleanField(
		default = True,
		help_text="Alerta de Luz",
		verbose_name="Alerta de Luz")
	ambient_alert = models.BooleanField(
		default = True,
		help_text="Alerta de Humedad Ambiental",
		verbose_name="Alerta de Humedad Ambiental")

	def __str__(self):
		return '{}'.format(self.id)


class SensorValue(models.Model):
	temperature = models.PositiveSmallIntegerField(verbose_name="Temperatura")
	humidity = models.PositiveSmallIntegerField(verbose_name="Humedad")
	light = models.PositiveSmallIntegerField(verbose_name="Luz")
	mov = models.PositiveSmallIntegerField(verbose_name="Movimiento")
	ambient = models.PositiveSmallIntegerField(verbose_name="Humedad Ambiental")
	
	def __str__(self):
		return '{}'.format(self.id)


class Log(models.Model):
	log = models.CharField(
		max_length=150, 
		verbose_name="Logs")

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return '({}) {}'.format(self.id, self.log)

