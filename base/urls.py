from django.urls import path
from . import views


urlpatterns = ([
    path('', views.home, name='home'),
    path('deities/', views.deities, name='deities'),
    path('creatures/', views.creatures, name='creatures'),
    path('heroes/', views.heroes, name='heroes'),
    path('shop/', views.shop, name='shop'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('add/<str:id>/', views.add, name='add'),
    path('delete/<str:id>/', views.delete, name='drop'),
    path('buy/<int:id>/', views.buy_now, name='buy_now'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete'),
    path('update_user/', views.update_user, name='update_user'),
    path('gallery/', views.gallery, name='gallery'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('image/<int:image_id>/', views.view_image, name='view_image'),
    path('delete_comment/<str:id>', views.delete_comment, name='delete_comment')
])

