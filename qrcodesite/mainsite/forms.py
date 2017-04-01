from django.forms import ModelForm
from django import forms

from .models import Traveller, Background



class TravellerForm(ModelForm):
	class Meta:
		model = Traveller
		fields = ('email',)

class BackgroundForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super(BackgroundForm, self).__init__(*args, **kwargs)
		self.fields['gender'].default = None
		# self.initial['gender'] = 'M'

	class Meta:
		model = Background
		fields = ('gender',)
		widgets = {
			'gender': forms.RadioSelect,
		}

	
