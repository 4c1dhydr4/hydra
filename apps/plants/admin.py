from django.contrib import admin
from apps.plants.models import Configuration

# Register your models here.
class ConfigurationAdmin(admin.ModelAdmin):
	list_display = ('id','active')

admin.site.register(Configuration, ConfigurationAdmin)