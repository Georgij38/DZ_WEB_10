from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date']


class RegisterForm(UserCreationForm):
    birth_date = forms.DateField(required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)