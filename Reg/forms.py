from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    type=forms.CharField(max_length=20)
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email', 'type', 'password1', )
