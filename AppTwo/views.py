from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Topic,Webpage

# Create your views here.
def help(request):
	
	webpage_name = Webpage.objects.all()
	my_dict = {'names' : webpage_name}
	# my_dict = {'insert_me' : ' hii i am from views'}
	return render(request, 'AppTwo/index.html' , context = my_dict)