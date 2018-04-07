from django import forms
from django.core import validators

class FormName(forms.Form):

	Name = forms.CharField()
	Email = forms.EmailField()
	botcatcher = forms.CharField(required = False, widget= forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])