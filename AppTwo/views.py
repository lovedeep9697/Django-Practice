from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help(request):
	
	my_dict = {'insert_me' : ' hii i am from views'}
	return render(request, 'AppTwo/index.html' , context = my_dict)