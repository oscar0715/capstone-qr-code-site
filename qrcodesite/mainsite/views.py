from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Traveller, Background, TravelPlan
from .forms import TravellerForm, BackgroundForm, TravelPlanForm

from .models import Area, Shop, ShopActivity
from .forms import ShopActivityForm

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

				return render(request, 'mainsite/next.html', {})

			except Traveller.DoesNotExist:
				# If there is no such email.
				
				# Register a new one 
				traveller = Traveller.objects.create(email = email)

				# User cookie to store the email
				request.session['email'] = email

				logging.debug("[welcome email ] = " + str(request.session.get('email', False)))

				return redirect('mainsite:background')

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

def background(request):
	if request.session.get('email', False):
		return redirect('mainsite:welcome')

	email = request.session.get('email', False)

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
	return render(request, 'mainsite/background.html', dict)

# Travel plan method
def travelPlan(request):
	if request.session.get('email', False):
		return redirect('mainsite:welcome')

	email = request.session.get('email', False)

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
def shopActivity(request):
	email = request.session.get('email', None)
	logging.debug("[email] = " + str(email))
	if email == None:
		return redirect('mainsite:welcome')

	# We have the traveller object now
	traveller = getTraveller(email)

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
			return next(request)

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



def next(request):
	return render(request, 'mainsite/next.html', {})
	