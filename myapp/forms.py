from django import forms
from django.contrib.auth.models import User
from myapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
	