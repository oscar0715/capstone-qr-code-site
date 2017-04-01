from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Traveller, Background
from .forms import TravellerForm, BackgroundForm

# Create your views here.

import logging
logger = logging.getLogger(__name__)

def index(request):
	return render(request, 'mainsite/index.html', {})

def securityGateWelcome(request):
	

	if request.method == 'GET' :
		form = TravellerForm()
		
	else :
		email = request.POST.get('email', None)
		form = TravellerForm(request.POST)

		if form.is_valid():
			try:
				traveller = Traveller.objects.get(email = email)
				# redict to another page
				return render(request, 'mainsite/next.html', {})

			except Traveller.DoesNotExist:
				# If there is no such email.
				
				# Register a new one 
				traveller = Traveller.objects.create(email = email)

				# User cookie to store the email
				request.session['email'] = email

				return redirect('mainsite:backgroundInfo')

	return render(request, 'mainsite/securityGateWelcome.html', {'form':form}) 

def backgroundInfo(request):
	email = request.session['email']
	try:
		traveller = Traveller.objects.get(email = email)
	except Traveller.DoesNotExist:
		traveller = Traveller.objects.create(email = email)

	background = Background.objects.filter(traveller=traveller)
	if background.count() == 0:
		
		form = BackgroundForm()
	else :
		form = BackgroundForm(instance = background[0])

	if request.method == "POST":
		form = BackgroundForm(request.POST)
		if form.is_valid():
			background = form.save(commit=False)
			background.traveller = traveller
			background.save()
			return next(request)

	dict = {
		'email' : email,
		'form' : form,
	}
	return render(request, 'mainsite/backgroundInfo.html', dict)

def next(request):
	return render(request, 'mainsite/next.html', {})
	