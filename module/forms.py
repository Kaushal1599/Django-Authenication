from django import forms
from django.contrib.auth.models import User

from module.models import UsertInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class ProfileForm(forms.ModelForm):
    class Meta():
        model = UsertInfo
        fields = ('Profile', 'profile_pic',)
