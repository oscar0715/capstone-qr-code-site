from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Traveller, Background, TravelPlan
from .forms import TravellerForm, BackgroundForm, TravelPlanForm

from .models import Area, Shop, ShopActivity
from .forms import ShopActivityForm

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

def getTraveller(email):
	try:
		traveller = Traveller.objects.get(email = email)
	except Traveller.DoesNotExist:
		traveller = Traveller.objects.create(email = email)
	return traveller

def getForm(traveller, Model, ModelForm):
	try :
		# aobject exits
		aobject = Model.objects.get(traveller=traveller)
		form = ModelForm(instance = aobject)
	except Model.DoesNotExist:
		# Object not exits
		aobject = Model.objects.create(traveller = traveller)
		form = ModelForm(instance = aobject)

	alist = [aobject, form]
	return alist

def backgroundInfo(request):
	email = request.session['email']

	# We have the traveller object now
	traveller = getTraveller(email)

	alist = getForm(traveller, Background, BackgroundForm)
	background = alist[0]
	form = alist[1]
		
	# We have the background object now

	if request.method == "POST":
		
		# create a for base on the background object
		form = BackgroundForm(request.POST, instance = background)
		if form.is_valid():
			# save update 
			form.save()
			return redirect('mainsite:travelPlan')

	dict = {
		'email' : email,
		'form' : form,
	}
	return render(request, 'mainsite/backgroundInfo.html', dict)

# Travel plan method
def travelPlan(request):
	email = request.session['email']

	# We have the traveller object now
	traveller = getTraveller(email)

	alist = getForm(traveller, TravelPlan, TravelPlanForm)
	travelPlan = alist[0]
	form = alist[1]
		
	# We have the travel plan object now

	if request.method == "POST":
		
		# create a for base on the travel plan object
		form = TravelPlanForm(request.POST, instance = travelPlan)
		if form.is_valid():
			# save update 
			form.save()
			return next(request)

	dict = {
		'email' : email,
		'form' : form,
	}
	return render(request, 'mainsite/travelPlan.html', dict)

# Shop Activity
# def shopActivity(request):
# 	email = request.session['email']

# 	# We have the traveller object now
# 	traveller = getTraveller(email)

# 	# alist = getForm(traveller, ShopActivity, ShopActivityForm)
# 	# shopActivity = alist[0]
# 	# form = alist[1]

# 	if request.method == "POST":
		
# 		# create a for base on the shop activity object
# 		form = TravelPlanForm(request.POST, instance = travelPlan)
		
# 		if form.is_valid():
# 			# save update 
# 			form.save()
# 			return next(request)

# 	dict = {
# 		'email' : email,
# 		'form' : form,
# 	}
# 	return render(request, 'mainsite/shopActivity.html', dict)

def next(request):
	return render(request, 'mainsite/next.html', {})
	