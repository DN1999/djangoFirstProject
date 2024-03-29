from django.shortcuts import render
from django.http import HttpResponse
# import django.http
# print(dir(django.http))

# Create your views here.

def home(request):
    # return HttpResponse("<h1>Krishna World</h1>");
    return render(request,"home.html",{"name":"सर्वांना"})

def add(request):
    val1= int(request.POST["num1"])
    val2= int(request.POST["num2"])
    res = val1+val2
    return render(request,"result.html",{"result":res})