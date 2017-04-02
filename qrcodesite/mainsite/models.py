from __future__ import unicode_literals

from django.db import models

from multiselectfield import MultiSelectField



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
	traveller = models.OneToOneField(
        Traveller,
        on_delete=models.CASCADE,
        primary_key=True,
    )

	# Status
	status_choices = (
		('S', "Students"),
		('E', "Employed"),
		('N', "Not currently employed"),
		('R', "Retired"),
		('O', "Other")
	)
	status = models.CharField( 
		max_length = 1,
		choices= status_choices, 
		verbose_name ='What is your status?', 
		default='Unspecified'
		)	
	other_status = models.CharField(
		max_length = 50, 
		blank = True)

	
	# Age
	age_choices = (
		('1', "1 - 25"),
		('2', "26 - 35"),
		('3', "36 - 50"),
		('5', "51+")
	)
	age = models.CharField( 
		max_length = 1,
		choices= age_choices, 
		verbose_name ='Which age group are you in?', 
		default='Unspecified'
		)


	# gender
	gender_choices = (
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other'),
		('N', 'I prefer not to specify')
	)

	gender = models.CharField(max_length=1, 
		choices=gender_choices, 
		verbose_name ='Your Gender:', 
		default='Unspecified')
	
	def __str__(self):
		return self.traveller.email 

class TravelPlan(TimeStampedModel):
	# Email
	traveller = models.OneToOneField(
        Traveller,
        on_delete=models.CASCADE,
        primary_key=True,
    )

	# Travel Purpose
	purpose_choices = (
		('L', "Leisure"),
		('B', "Business"),
		('O', "Other")
	)
	purpose = models.CharField( 
		max_length = 1,
		choices= purpose_choices, 
		verbose_name ='What is the purpose for this air trip?', 
		default='Unspecified'
		)
	other_purpose = models.CharField(
		max_length = 50, 
		blank = True)

	# Group / self plan
	group_choices = (
		('G', "Group"),
		('S', "Self-planned"),

	)
	group = models.CharField( 
		max_length = 1,
		choices= group_choices, 
		verbose_name ='Are you in an organized traveling group or self-planned traveler?', 
		default='Unspecified'
		)

	# Group number
	group_number_choices = (
		('0', "Travel alone"),
		('1', "1-2"),
		('3', "3-4"),
		('5', "5-10"),
		('11', "11+"),
	)
	group_number = models.CharField( 
		max_length = 2,
		choices= group_number_choices, 
		verbose_name ='How many people are you traveling with?', 
		default='Unspecified'
		)

	# time period
	time_period_choices = (
		('M', "Morning"),
		('A', "Afternoon"),
		('E', "Evening"),
		('L', "Late Night"),
	)
	time_period = models.CharField( 
		max_length = 2,
		choices= time_period_choices, 
		verbose_name ='During which time period will your flight depart from Pittsburgh International Airport?', 
		default='Unspecified'
		)

	# How often
	how_often_choices = (
		('W', "Once a Week"),
		('M', "Once a Month"),
		('HY', "Once every 6 months"),
		('LY', "Less often than once a year"),
		('Y', "Once a year"),
	)
	how_often = models.CharField( 
		max_length = 2,
		choices= how_often_choices, 
		verbose_name ='How often do you fly from Pittsburgh International Airport?', 
		default='Unspecified'
		)

	# AirLines
	airline_choices = (
		('AC', "Air Canada"),
		('AL', "Allegiant"),
		('AA', "American Airlines"),
		('CO', "Condor"),
		('DA', "Delta Air Lines"),
		('JB', "JetBlue"),
		('FR', "Frontier"),
		('OJ', "OneJet"),
		('PO', "Porter"),
		('SW', "Southwest"),
		('SA', "Southern Airways Express"),
		('UA', "United Airlines"),
		('WO', "WOW"),
		('O', "other"),
	)
	airline = models.CharField( 
		max_length = 2,
		choices= airline_choices, 
		verbose_name ='What airline are you traveling on?', 
		)

	def __str__(self):
		return self.traveller.email 