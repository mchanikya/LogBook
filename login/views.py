from django.shortcuts import render
from django.http import HttpResponse
from .models import userLogin
import json

# Create your views here.
def index(request):
	if request.method=='POST':
		# print(json.loads(request.body.decode("utf-8")))
		data=json.loads(request.body.decode("utf-8"))
		# print(data)
		usr=userLogin()
		usr.setName(data['name'])
		usr.setEmail(data['email'])
		usr.setPass(data['password'])
		usr.save()
	# x=userLogin.objects.all()
	# print(x)
	return HttpResponse("Congs! Account Created")