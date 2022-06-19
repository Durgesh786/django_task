from django import forms
from django.contrib.auth.forms import PasswordChangeForm, AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm
from web.user.models import AddEmails


class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6)
    phone_number = forms.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super(OTPForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update(
            {'class': 'form-control input-lg', 'type': 'number', 'placeholder': 'Phone number'}, required=True)
        self.fields['otp'].widget.attrs.update(
            {'class': 'form-control input-lg', 'placeholder': 'OTP'}, required=True)


class RegisterForm(forms.Form):
    phone_number = forms.IntegerField()
    email = forms.EmailField()
    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput())
    re_password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control input-lg', 'type': 'email', 'placeholder': 'Email'}, required=True)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control input-lg', 'placeholder': 'Select Username'}, required=True)
        self.fields['phone_number'].widget.attrs.update(
            {'class': 'form-control input-lg', 'type': 'number', 'placeholder': 'Phone number'}, required=True)
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control input-lg', 'type': 'password', 'placeholder': "Password"})
        self.fields['re_password'].widget.attrs.update(
            {'class': 'form-control input-lg', 'type': 'password', 'placeholder': "Confirm Password"})


class LoginForm(forms.Form):
    phone_number = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update(
            {'class': 'form-control input-lg', 'type': 'number', 'placeholder': 'Phone number'}, required=True)


class AddEmailForm(forms.Form):
    email = forms.CharField()
    is_primary = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(AddEmailForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control input-lg', 'type': 'email', 'placeholder': 'Enter Email'}, required=True)
        self.fields['is_primary'].widget.attrs.update(
            {'class': 'form-control input-lg', 'placeholder': 'OTP'})


