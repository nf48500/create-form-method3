from django.shortcuts import render
from .models import Product

# Create your views here.
def product (request):
    return render(request,'products/product.html')

def products(request):
    product_list =Product.objects.all()  
    x={'pro': product_list.filter(price=200)} 
    return render(request, 'products/products.html',x)