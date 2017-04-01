from __future__ import unicode_literals

from django.db import models



# Create your models here.
class TimeStampedModel(models.Model):
	"""
	abstract base class
	"""
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class Traveller(TimeStampedModel):
	# basic
	email = models.EmailField(max_length=254,
		# null = False,
		blank = False,
		verbose_name ='Email')

	def __str__(self):
		return self.email 

class Background(TimeStampedModel):
	# Email
	traveller = models.ForeignKey(Traveller)

	# Status
	status_choices = (
		('S', "Students"),
		('E', "Employed"),
		('N', "Not currently employed"),
		('R', "Retired"),
		('O', "Other")
	)


	# gender
	gender_choices = (
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other'),
		('N', 'I prefer not to specify')
	)
	
	gender = models.CharField(max_length=1, choices=gender_choices, verbose_name ='Gender', default='Unspecified')
	
	def __str__(self):
		return self.traveller.email 