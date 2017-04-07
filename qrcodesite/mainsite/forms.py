from django.forms import ModelForm
from django import forms

from .models import Traveller, Background, TravelPlan
from .models import Area, Shop, ShopActivity, AirportActivity



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
			'airline': forms.Select(attrs={'class':'browser-default'})
		}

class ShopActivityForm(ModelForm):
	class Meta:
		model = ShopActivity
		exclude = ['traveller']
		widgets = {
			'spending': forms.RadioSelect,
			'area': forms.Select(attrs={'class':'browser-default'}),
			'shop': forms.Select(attrs={'class':'browser-default'})
		}

class AirportActivityForm(ModelForm):
	class Meta:
		model = AirportActivity
		exclude = ['traveller']
		widgets = {
			'leisure_time': forms.RadioSelect,
			'shopping_spending': forms.RadioSelect,
			'coffee_shop_spending': forms.RadioSelect,
			'bar_spending': forms.RadioSelect,
			'news_spending': forms.RadioSelect,
			'kidsport_spending': forms.RadioSelect,
			'other_spending': forms.RadioSelect,
			# 'will_visit' : forms.RadioSelect,
			'why_not' : forms.RadioSelect,
		}
	