from django.contrib.auth.forms import UserCreationForm
from .models import User, Product
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['picture', 'name', 'price', 'currency', 'description']
