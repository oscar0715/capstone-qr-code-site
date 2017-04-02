from . import views 

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

app_name = 'mainsite'


urlpatterns = [
	url(r'^index$', views.index, name='index'),
	url(r'^welcome$', views.securityGateWelcome, name='welcome'),
	url(r'^backgroundinfo/$', views.backgroundInfo, name='backgroundInfo'),
	url(r'^travelplan/$', views.travelPlan, name='travelPlan')
]