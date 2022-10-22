from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.style import context
from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customers.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(status = 'Delivered').count()
    
    pending = orders.filter(status = 'PENDING').count()

    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending}

    return render(request,'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})


def customer(request):
    return render(request,'accounts/customer.html')