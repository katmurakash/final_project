from django.shortcuts import render
from .models import God

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def deities(request):
    gods = God.objects.all()
    context = {"gods": gods}
    return render(request, 'base/deities.html', context)


def creatures(request):
    return render(request, 'base/creatures.html')

def heroes(request):
    return render(request, 'base/heroes.html')

def shop(request):
    return render(request, 'base/shop.html')

