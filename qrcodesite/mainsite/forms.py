from django.forms import ModelForm
from django import forms

from .models import Traveller, Background, TravelPlan
from .models import Area, Shop, ShopActivity



class TravellerForm(ModelForm):
	class Meta:
		model = Traveller
		fields = ('email',)

class BackgroundForm(ModelForm):

	class Meta:
		model = Background
		exclude = ['traveller']
		widgets = {
			'gender': forms.RadioSelect,
			'status': forms.RadioSelect,
			'age': forms.RadioSelect,
		}

class TravelPlanForm(ModelForm):
	class Meta:
		model = TravelPlan
		exclude = ['traveller']
		widgets = {
			'purpose': forms.RadioSelect,
			'group': forms.RadioSelect,
			'group_number': forms.RadioSelect,
			'time_period': forms.RadioSelect,
			'how_often': forms.RadioSelect,
		}

class ShopActivityForm(ModelForm):
	class Meta:
		model = ShopActivity
		exclude = ['traveller']
		widgets = {
			'spending': forms.RadioSelect,
		}
	
