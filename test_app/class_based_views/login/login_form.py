__author__ = 'zschweinfurth'

from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(max_length=30, label='Username', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        return cleaned_data