from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('products/',views.products),
    path('customer/<str:pk_test>/',views.customer)
]
