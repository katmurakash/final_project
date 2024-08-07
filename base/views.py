from django.shortcuts import render
from .models import God, Product, Hero, Creature, User, Type
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def deities(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    gods = God.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
    context = {"gods": gods}
    return render(request, 'base/deities.html', context)


def creatures(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    creatures = Creature.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
    context = {"creatures": creatures}
    return render(request, 'base/creatures.html', context)

def heroes(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    heroes = Hero.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
    context = {"heroes": heroes}
    return render(request, 'base/heroes.html', context)

def shop(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(type__name__icontains=q))
    products = list(set(products))
    heading = "Products"
    types = Type.objects.all()
    context = {"products": products, "heading": heading, 'types': types}
    return render(request, 'base/shop.html', context)

def profile(request, pk):
    user = User.objects.get(id=pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = user.products.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(type__name__icontains=q))
    products = list(set(products))
    heading = "My Products"
    types = Type.objects.all()
    context = {"products": products, "heading": heading, 'types': types}
    return render(request, 'base/profile.html', context)


