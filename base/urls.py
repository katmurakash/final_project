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
    path('profile/<str:pk>/', views.profile, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
