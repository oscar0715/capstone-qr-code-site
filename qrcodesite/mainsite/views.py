from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Traveller, Background, TravelPlan
from .forms import TravellerForm, BackgroundForm, TravelPlanForm

from .models import Area, Shop, ShopActivity, AirportActivity
from .forms import ShopActivityForm, AirportActivityForm

import json

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
				request.session['email'] = email

				return redirect('mainsite:thankyou')

			except Traveller.DoesNotExist:
				# If there is no such email.
				
				# Register a new one 
				traveller = Traveller.objects.create(email = email)

				# User cookie to store the email
				request.session['email'] = email

				# logging.debug("[welcome email ] = " + str(request.session.get('email', False)))

				return redirect('mainsite:background')

	return render(request, 'mainsite/securityGateWelcome.html', {'form':form}) 

def getTraveller(email):
	try:
		traveller = Traveller.objects.get(email = email)
	except Traveller.DoesNotExist:
		traveller = Traveller.objects.create(email = email)
	return traveller


def background(request):
	email = request.session.get('email', None)
	if email == None:
		return redirect('mainsite:welcome')

	# We have the traveller object now
	traveller = getTraveller(email)

	background = None
	try:
		background = Background.objects.get(traveller = traveller)
		form = BackgroundForm(instance=background)
	except Background.DoesNotExist:
		form = BackgroundForm()
		# logging.debug("[background] = "+"None")

	if request.method == "POST":

		form = BackgroundForm(request.POST)
		if form.is_valid():

			# save update 
			background = form.save(commit=False)
			background.traveller = traveller
			background.save()
			return redirect('mainsite:travelPlan')

	dict = {
		'email' : email,
		'form' : form,
	}
	return render(request, 'mainsite/background.html', dict)

# Travel plan method
def travelPlan(request):
	email = request.session.get('email', None)
	if email == None:
		return redirect('mainsite:welcome')

	# We have the traveller object now
	traveller = getTraveller(email)

	# check whether has Backgound Object
	try:
		background = Background.objects.get(traveller = traveller)
	except Background.DoesNotExist:
		return redirect('mainsite:background')

	travelPlan = None
	try:
		travelPlan = TravelPlan.objects.get(traveller = traveller)
		form = TravelPlanForm(instance = travelPlan)
	except TravelPlan.DoesNotExist:
		travelPlan = TravelPlan.objects.create(traveller = traveller)
		form = TravelPlanForm(instance = travelPlan)
		
	# We have the travel plan object now

	if request.method == "POST":
		
		# create a for base on the travel plan object
		form = TravelPlanForm(request.POST, instance = travelPlan)

		if form.is_valid():
			# save update 
			logging.debug("[bugTag] = " + "2")
			form.save()

			# check whether visited airportactivity page
			airportactivityVisited = request.session.get('airportactivity', None)
			if not airportactivityVisited == None:
				return redirect('mainsite:airportActivity')

			# check whether visited shopactivity page
			shopactivityVisited = request.session.get('shopactivity', None)
			if shopactivityVisited == None:
				return redirect('mainsite:thankyou')
			else :
				logging.debug("[bugTag] = " + "2")
				return redirect('mainsite:shopActivity')
			
	dict = {
		'email' : email,
		'form' : form,
	}
	return render(request, 'mainsite/travelPlan.html', dict)

# Shop Activity
def shopActivity(request):

	#  Mark Visited
 	request.session['shopactivity'] = True

 	# Check whether have email
	email = request.session.get('email', None)
	if email == None:
		# if not go to register one
		return redirect('mainsite:welcome')

	# We have the traveller object now
	traveller = getTraveller(email)

	# Check backgournd
	try :
		# background exits
		background = Background.objects.get(traveller=traveller)
		# this Ok
	except Background.DoesNotExist:
		# background not exits
		# go to the background page
		return redirect('mainsite:background')

	# check Travel Plan
	try :
		# Travel Plan exits
		travelPlan = TravelPlan.objects.get(traveller=traveller)
		# this Ok
	except TravelPlan.DoesNotExist:
		# Travel Plan not exits
		# go to Travel Plan
		return redirect('mainsite:travelPlan')

	form = ShopActivityForm()

	if request.method == "POST":
		areaId = request.POST.get('area')
		shopId = request.POST.get('shop')

		area = get_object_or_404(Area, pk = areaId)
		shop = get_object_or_404(Shop, pk = shopId)

		try:
			shopActivity = ShopActivity.objects.get(
			traveller=traveller,
			shop = shop)
		except ShopActivity.DoesNotExist:
			shopActivity = ShopActivity.objects.create(
				traveller = traveller,
				shop = shop,
				area = area)
		
		# create a for base on the shop activity object
		form = ShopActivityForm(request.POST, instance = shopActivity)
		
		if form.is_valid():
			# save update 
			form.save()
			return redirect('mainsite:thankyou')

	dict = {
		'email' : email,
		'form' : form,
	}
	return render(request, 'mainsite/shopActivity.html', dict)

def getShopList(request):
	results = Shop.objects.none()

	areaId = request.GET.get('areaId', None)
	area = get_object_or_404(Area, pk = areaId)

	# get all the provinces
	shops = Shop.objects.filter(area = area)
	
	list = []
	for shop in shops:
		c = {}
		c['name'] = shop.name
		c['shopId'] = shop.pk
		list.append(c)

	return HttpResponse(json.dumps(list),content_type = "application/json;charset=utf-8")

def getShopSpending(request):

	email = request.session.get('email', None)
	traveller = get_object_or_404(Traveller, email = email)

	shopId = request.GET.get('shopId', None)
	shop = get_object_or_404(Shop, pk = shopId)
	
	shopActivity = None
	try:
		shopActivity = ShopActivity.objects.get(traveller = traveller, shop = shop)

	except ShopActivity.DoesNotExist:
		return HttpResponse(json.dumps({}),content_type = "application/json;charset=utf-8")

	spending = shopActivity.spending
	
	dict = {
		"value" : spending
	}
	return HttpResponse(json.dumps(dict),content_type = "application/json;charset=utf-8")

# Airport Activity method
def airportActivity(request):
	#  Mark Visited
 	request.session['airportactivity'] = True

	email = request.session.get('email', None)
	if email == None:
		return redirect('mainsite:welcome')

	# We have the traveller object now
	traveller = getTraveller(email)

	# check whether has Backgound Object
	try:
		background = Background.objects.get(traveller = traveller)
	except Background.DoesNotExist:
		return redirect('mainsite:background')

	airportActivity = None
	try:
		airportActivity = AirportActivity.objects.get(traveller = traveller)
		form = AirportActivityForm(instance = airportActivity)
	except AirportActivity.DoesNotExist:
		airportActivity = AirportActivity.objects.create(traveller = traveller)
		form = AirportActivityForm(instance = airportActivity)
		
	# We have the Airport Activity object now

	if request.method == "POST":
		
		# create a for base on the Airport Activity object
		form = AirportActivityForm(request.POST, instance = airportActivity)
		if form.is_valid():
			# save update 
			form.save()

			return redirect('mainsite:thankyou')
			
	dict = {
		'email' : email,
		'form' : form,
	}
	return render(request, 'mainsite/airportActivity.html', dict)

def thankyou(request):
	email = request.session.get('email', None)

	return render(request, 'mainsite/thankyou.html', {'email':email})

def thankyouAfterShop(request):
	email = request.session.get('email', None)

	return render(request, 'mainsite/thankyoushop.html', {'email':email})
	