from django import forms

class LoginFrom(forms.Form):
    username=forms.CharField (max_length=30)
    password=forms.CharField(widget=forms.PasswordInput)