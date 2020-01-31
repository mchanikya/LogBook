from django.db import models

# Create your models here.

class UserProfile(models.Model):
	FirstName = models.CharField(max_length=100)
	MiddleName = models.CharField(max_length=100)
	LastName = models.CharField(max_length=100)
	FullName = models.CharField(max_length=300)
	PermanentAddress = models.CharField(max_length=200)
	MailingAddress = models.CharField(max_length=200)
	DOB = models.DateField(max_length=8)
	"""docstring Details Name"""
	# def __init__(self, arg):
	# 	self.arg = arg
		
	def __str__(self):
		return self.FullName
