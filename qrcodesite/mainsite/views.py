from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'mainsite/index.html', {})

def welcome(request):
	return render(request, 'mainsite/welcome.html', {})