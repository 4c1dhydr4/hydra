from django.shortcuts import render
from apps.plants.models import Log

def index(request):
	context = {
		'logs': Log.objects.all(),
	}
	return render(request, 'index.html',context)