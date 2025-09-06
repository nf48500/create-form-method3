from django.shortcuts import render
from .models import Login
from .forms import Loginform
# Create your views here.
def home(request):
    return render(request,'pages/home.html')
def form(request):
    if request.method == 'POST':
       if request.method == 'post':
           dataform=Loginform (request.post)
           if dataform.is_valid():
               dataform.save()
    return render(request, 'pages/form.html',{'lf':Loginform()})
