from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop-login'),
    path('home/', views.home, name='shop-home'),
    path('about/', views.about, name='shop-about'),
    path('contact/', views.contact, name='shop-contact'),
    path('account/', views.account, name='shop-account'),
    path('productview/<int:myid>', views.productview, name = 'shop-productview'),
]