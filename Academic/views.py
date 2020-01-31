from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
	# question_list = Question.objects.order_by('-pub_date')[:5]
	return HttpResponse("You're at the Academic index.")
	# render(request,'polls/index.html',{'question_list':question_list})
