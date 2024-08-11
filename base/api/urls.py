from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='get_routes'),
    path('products', views.get_products, name='get_products'),
    path('products/<int:id>', views.get_product, name='get_product'),
    path('images', views.get_images, name='get_images'),
    path('images/<int:id>', views.get_image, name='get_image'),
]
