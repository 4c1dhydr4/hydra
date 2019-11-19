from django.contrib import admin
from apps.plants.models import (Configuration, SensorValue, Log,)

# Register your models here.
class ConfigurationAdmin(admin.ModelAdmin):
	list_display = ('id','active')
class SensorValueAdmin(admin.ModelAdmin):
	list_display = ('id',)
class LogAdmin(admin.ModelAdmin):
	list_display = ('id',)


admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(SensorValue, SensorValueAdmin)
admin.site.register(Log, LogAdmin)