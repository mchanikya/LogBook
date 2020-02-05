from django.shortcuts import render
from django.http import HttpResponse
from .models import userLogin
import json

# Create your views here.
def index(request):
	if request.method=='POST':
		# print(json.loads(request.body.decode("utf-8")))
		data=json.loads(request.body.decode("utf-8"))
		for i in data:
			print(data[i])
	return HttpResponse("Congs! Account Created")