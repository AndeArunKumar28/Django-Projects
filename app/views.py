from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog

# Create your views here.

def Home(request):
    post=Blog.objects.all()
    return render(request,"base.html",{'post':post})

def Demo(request):
    return HttpResponse("Try and Try until you success")
