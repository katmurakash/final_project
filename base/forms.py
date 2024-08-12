from django.contrib.auth.forms import UserCreationForm
from .models import User, Product, Image
from django import forms
from django.forms import ModelForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['picture', 'name', 'price', 'currency', 'description']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'email', 'bio', 'products']


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'artist', 'image']