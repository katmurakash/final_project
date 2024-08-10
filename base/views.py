from django.shortcuts import render, redirect, get_object_or_404
from .models import God, Product, Hero, Creature, User, Type
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, ProductForm
from .seeder import seeder_func
from django.contrib import messages
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
    seeder_func()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(type__name__icontains=q))
    products = list(set(products))
    heading = "Products"
    types = Type.objects.all()
    context = {"products": products, "heading": heading, 'types': types}
    return render(request, 'base/shop.html', context)


@login_required(login_url='login')
def profile(request, pk):
    user = User.objects.get(id=pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = user.products.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(type__name__icontains=q))
    products = list(set(products))
    heading = "My Products"
    types = Type.objects.all()
    context = {"products": products, "heading": heading, 'types': types}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def add(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    user.products.add(product)
    return redirect('profile', request.user.id)


@login_required(login_url='login')
def delete(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    user.products.remove(product)
    return redirect('profile', request.user.id)


@login_required(login_url='login')
def buy_now(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'base/buy_now.html', {'product': product})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profile', request.user.id)

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            messages.error(request, 'User or Password is not correct!')

    return render(request, 'base/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    form = MyUserCreationForm

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('profile', user.id)

        else:
            messages.error(request, 'Follow the instructions and create proper user and password!')

    context = {'form': form}
    return render(request, 'base/register.html', context)


@login_required(login_url='login')
def add_product(request):
    types = Type.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product_type = request.POST.get('type')
            type_obj, created = Type.objects.get_or_create(name=product_type)

            new_product = form.save(commit=False)
            new_product.creator = request.user
            new_product.picture = request.FILES.get('picture')
            new_product.save()
            new_product.type.add(type_obj)

            return redirect('shop')

    context = {'form': form, 'types': types}
    return render(request, 'base/add_product.html', context)


@login_required(login_url='login')
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.picture.delete()
        product.delete()
        return redirect('shop')

    return render(request, 'base/delete.html', {'obj': product})
