from django.db import models

# Create your models here.

class God(models.Model):
    picture = models.ImageField(upload_to='gods/')
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}"
