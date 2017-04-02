from . import views 

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

app_name = 'mainsite'


urlpatterns = [
	url(r'^index$', views.index, name='index'),
	url(r'^welcome$', views.securityGateWelcome, name='welcome'),
	url(r'^background/$', views.background, name='background'),
	url(r'^travelplan/$', views.travelPlan, name='travelPlan'),
	url(r'^shopactivity/$', views.shopActivity, name='shopActivity'),
	url(r'^getShopList/$', views.getShopList, name='getShopList'),
	url(r'^getShopSpending/$', views.getShopSpending, name='getShopSpending'),
	url(r'^thankyou/$', views.thankyou, name='thankyou'),
]