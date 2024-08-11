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
    creator = models.ForeignKey('User', on_delete=models.SET("Unknown Creator"))
    picture = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    description = models.TextField(max_length=500)
    type = models.ManyToManyField(Type, related_name='products', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        types = ', '.join([type.name for type in self.type.all()])
        return f"{self.name} - {types}"


class User(AbstractUser):
    products = models.ManyToManyField(Product, related_name='users', blank=True)
    avatar = models.ImageField(null=True, default='avatar.svg')
    bio = models.TextField(null=True)

class Image(models.Model):
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body
