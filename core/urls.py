from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('about-us', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('products', views.products, name='products'),
    path('news', views.news, name='news'),
    path('news/<str:slug>', views.post, name='post')
]
