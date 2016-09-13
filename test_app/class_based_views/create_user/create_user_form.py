__author__ = 'zschweinfurth'

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class CreateUserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    password = forms.CharField(max_length=20, label='Password', required=True, widget=forms.PasswordInput)

    # call parent clean method so instances can return their data
    # simple call to parent without any custom parsing/cleaning of data
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        return cleaned_data


    """username = forms.CharField(max_length=30, label='Username')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    password = forms.CharField(max_length=30, label='Password')"""
