# from django import forms
# from django.core import validators

# class FormName(forms.Form):

# 	Name = forms.CharField()
# 	Email = forms.EmailField()
# 	botcatcher = forms.CharField(required = False, widget= forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])

from django import forms
from django.contrib.auth.models import User	
from AppTwo.models import UserProfileInfo


class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username','email', 'password')



class UserProfileInfo(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('portfolio_site', 'profile_pic')

