#forms.py
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
	username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("Must contain only letters, numbers and underscores. Try again!") })
	email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
	 
	def clean_username(self):
		try:
			user = User.objects.get(username__iexact=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
		raise forms.ValidationError(_("Sorry, that username already exists. Try another!"))
 
	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_("Whoops! The two password fields did not match."))
		return self.cleaned_data
	
		
		