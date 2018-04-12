from django.shortcuts import render
from django.http import HttpResponse
# from AppTwo.models import Topic,Webpage
from AppTwo.forms import UserForm, UserProfileInfoForm

# Create your views here.
# def help(request):
	
# 	webpage_name = Webpage.objects.all()
# 	my_dict = {'names' : webpage_name}
# 	# my_dict = {'insert_me' : ' hii i am from views'}
# 	return render(request, 'AppTwo/index.html' , context = my_dict)

# def help(request):
	
# 	return render(request, 'AppTwo/index.html' )


# def form_view(request):
# 	form = forms.FormName()

# 	return render(request, 'AppTwo/forms.html', {'form' : form})


def index(request):
	return render(request,'AppTwo/index.html')

def register(request):

	registered = False

	if(request.method == 'post'):
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileInfoForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid() :
			user = user_form.save()
			user.set_password(user.password)
			user.save()


			profile = profile_form.save(commit = False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered = True

		else:
			print(user_form.errors,profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()


	return render(request , 'AppTwo/register.html',
								{'user_form' : user_form,
								 'profile_form':profile_form,
								 'registered' : registered
								})