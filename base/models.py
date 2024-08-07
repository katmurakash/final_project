from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class God(models.Model):
    picture = models.ImageField(upload_to='gods/')
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    def __str__(self):
        return f"{self.name}"
class Creature(models.Model):
    picture = models.ImageField(upload_to='creatures/')
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    def __str__(self):
        return f"{self.name}"
class Hero(models.Model):
    picture = models.ImageField(upload_to='heroes/')
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    def __str__(self):
        return f"{self.name}"

class Type(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Product(models.Model):
    picture = models.ImageField(upload_to='shop/')
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    description = models.TextField(max_length=500)
    type = models.ManyToManyField(Type, related_name='products', blank=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    products = models.ManyToManyField(Product, related_name='users', blank=True)


