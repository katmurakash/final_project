from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('deities/', views.deities, name='deities'),
    path('creatures/', views.creatures, name='creatures'),
    path('heroes/', views.heroes, name='heroes'),
    path('shop/', views.shop, name='shop'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('add/<str:id>/', views.add, name='add'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('buy/<int:id>/', views.buy_now, name='buy_now'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
