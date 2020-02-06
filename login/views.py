from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import userLogin
import json

# Create your views here.
def index(request):
	if request.method=='POST':
		# print(json.loads(request.body.decode("utf-8")))
		data=json.loads(request.body.decode("utf-8"))
		# print(data)
		print(userLogin.objects.filter(email=data['email']).count())
		if 0 == userLogin.objects.filter(email=data['email']).count():
			usr=userLogin()
			usr.setName(data['name'])
			usr.setEmail(data['email'])
			usr.setPass(data['password'])
			usr.save()
			return JsonResponse({"message":"Congs! Account Created","status":True})
		else:
			return JsonResponse({"message":"Failed! Account already exist","status":False})
			# return HttpResponse("Failed! Account already exist")
	# x=userLogin.objects.all()
	# print(x)