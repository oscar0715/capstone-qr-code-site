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
		default='Unspecified',
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

# Travel Plan
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



# Area
class Area(TimeStampedModel):
	
	name = models.CharField( 
		max_length = 50,
		verbose_name ='Name', 
	) 
	def __str__(self):
		return self.name

# Shop
class Shop(TimeStampedModel):
	# Area
	area = models.ForeignKey(
		'Area',
		on_delete=models.CASCADE,
	)

	name = models.CharField( 
		max_length = 50,
		verbose_name ='Name', 
	) 
	def __str__(self):
		return self.name

class ShopActivity(TimeStampedModel):
	# Traveller
	traveller = models.ForeignKey(
		'Traveller',
		on_delete=models.CASCADE,
		default='Unspecified',
		null=False
	)

	area = models.ForeignKey(
		'Area',
		on_delete=models.CASCADE,
		verbose_name ='Please choose your Area', 
		default='Unspecified',
		null=False
	)

	shop = models.ForeignKey(
		'Shop',
		on_delete=models.CASCADE,
		verbose_name ='Please choose your Shop', 
		default='Unspecified',
		null=False
	)

	# Spending
	spending_choices = (
		('0', "$0 - $25"),
		('25', "$25 - $50"),
		('50', "$50 - $100"),
		('100', "$100+"),
	)
	spending = models.CharField( 
		max_length =3,
		choices= spending_choices, 
		verbose_name ='Please choose your spending at the shopping area you have visited', 
		default='Unspecified',
		blank=False
		)


	def __str__(self):
		return self.traveller.email 
		
class AirportActivity(TimeStampedModel):
	# Traveller
	traveller = models.OneToOneField(
		Traveller,
		on_delete=models.CASCADE,
		primary_key=True,
	)

	# leisure_time
	time_choices = (
		('0', "< 30min"),
		('0.5', "30min - 1h"),
		('1', "1h - 2h"),
		('2', "2h +"),
	)
	leisure_time = models.CharField( 
		max_length =3,
		choices= time_choices, 
		verbose_name ='How much leisure time do you have before boarding?', 
		default='Unspecified',
		blank=False
		)

	# spending_choices
	spending_choices = (
		('-1', "I didn't visit this place."),
		('0', "$0"),
		('1', "$0 - $25"),
		('25', "$25 - $50"),
		('50', "$50 - $100"),
		('100', "$100+"),
	)

	shopping_spending = models.CharField( 
		max_length =3,
		choices= spending_choices, 
		verbose_name ='Shopping', 
		default='Unspecified',
		blank=False
		)

	coffee_shop_spending = models.CharField( 
		max_length =3,
		choices= spending_choices, 
		verbose_name ='Coffee Shop', 
		default='Unspecified',
		blank=False
		)

	bar_spending = models.CharField( 
		max_length =3,
		choices= spending_choices, 
		verbose_name ='Bar/Dining', 
		default='Unspecified',
		blank=False
		)
	news_spending = models.CharField( 
		max_length =3,
		choices= spending_choices, 
		verbose_name ='News/Gift/Book Shop', 
		default='Unspecified',
		blank=False
		)
	kidsport_spending = models.CharField( 
		max_length =3,
		choices= spending_choices, 
		verbose_name ="KidsPort (Children's Play Area)", 
		default='Unspecified',
		blank=False
		)
	other_spending = models.CharField( 
		max_length =3,
		choices= spending_choices, 
		verbose_name ='Other', 
		default='Unspecified',
		blank=False
		)

	other_name = models.CharField( 
		max_length =50,
		verbose_name ='If you choose "other" in the places you have visited, please specify', 
		blank=True
		)

	# Why Not
	why_not_choices = (
		('A', "Shops far from waiting area"),
		('B', "Shops are not appealing"),
		('C', "Do not have enough time"),
		('D', "Prefer to be at my gate"),
		('E', "Too expensive"),
		('F', "Other"),
	)

	why_not = models.CharField( 
		max_length =1,
		choices= why_not_choices, 
		verbose_name ='If you did not visit any of these areas, why not?', 
		blank = True,
		)

	other_why_not = models.CharField( 
		max_length =200,
		verbose_name ='If you choose "other" in the places you have visited, please specify', 
		blank=True
		)

	# will visit
	will_visit_choices = (
		('A', "Shopping (Apparels, Cosmetics, duty-free etc.)"),
		('B', "Coffee Shop"),
		('C', "Bar/Dining"),
		('D', "News/Gift/Book Shop"),
		('E', "Convenience Store"),
		('F', "Vending Machine"),
		('G', "KidsPort (Children's Play Area)"),
		('H', "24*7 Grocery Store"),
		('I', "Other"),
	)

	will_visit = MultiSelectField( 
		max_length = 10,
		choices = will_visit_choices, 
		verbose_name ='Where would you like to visit if you have enough time? Please choose your top 3 preferences.', 
		blank = True,
		)

	other_will_visit = models.CharField( 
		max_length =200,
		verbose_name ='', 
		blank=True
		)

	# ask for other service
	other_service = models.CharField( 
		max_length =300,
		verbose_name ='Other than the places listed above, what other services would you like to have at the airport?', 
		blank=True
		)

	def __str__(self):
		return self.traveller.email 


