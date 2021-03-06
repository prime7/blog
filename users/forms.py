from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .validators import validateEmail


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(validators = [validateEmail])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'website','github','youtube']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
