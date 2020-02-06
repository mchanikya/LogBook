from django.db import models

# Create your models here.
class userLogin(models.Model):
	"""docstring for userLogin"""
	name=models.CharField(max_length=100,default="")
	email=models.CharField(max_length=100,default="")
	password=models.CharField(max_length=100,default="")

	# def __init__(self):
	# 	self.name = ""
	# 	self.email = ""
	# 	self.password = ""

	def __str__(self):
		return self.name

	def setName(self,name):
		self.name=name

	def setEmail(self,email):
		self.email=email

	def setPass(self,password):
		self.password=password

	def display(self):
		print("name: ",self.name)
		print("email: ",self.email)
		print("passw: ",self.password)