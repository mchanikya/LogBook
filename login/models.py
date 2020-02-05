from django.db import models

# Create your models here.
class userLogin:
	"""docstring for userLogin"""
	def __init__(self,name,email,password):
		super(userLogin, self).__init__()
		self.name = name
		self.email = email
		self.password = password