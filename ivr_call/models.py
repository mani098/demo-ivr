from django.db import models
from model_utils import Choices

class PhoneModel(models.Model):

	phone_number = models.CharField(max_length=20)
	welcome_message = models.CharField(max_length=100)

	def __unicode__(self):
		return self.phone_number

class IvrModel(models.Model):
	
	ivr_choices = Choices('Redirect to', 'Add Speak')
	
	phone = models.ForeignKey(PhoneModel)

	ivr_option = models.CharField(max_length=30)
	option_type = models.CharField(max_length=20, choices=ivr_choices, default='Redirect to')
	option_value = models.CharField(max_length=40, null=True)

	def __unicode__(self):
		return self.ivr_option