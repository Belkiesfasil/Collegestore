from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from tkinter import *
from tkinter import messagebox


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('loginapp:loggedin')
        else:
                messages.info(request,"invalid credentials")
                return redirect('loginapp:login')
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('loginapp:register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"email already exists")
                 return redirect('loginapp:register')
            else:
                 user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                 user.save()
                 return redirect('loginapp:login')
                 print("user registered")


        else:
            messages.info(request,"password not matching")
            return redirect('loginapp:register')

        return redirect('loginapp:login')

    return render(request,"register.html")
def loggedin(request):

    return render(request,"loggedin.html")

def details(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        date = request.POST.get('date','')
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('loginapp:details')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('loginapp:details')
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                return redirect('loginapp:order')
                print("user registered")

        else:
            messages.info(request, "password not matching")
            return redirect('loginapp:details')

        return redirect('loginapp:order')

    return render(request,"details.html")
def order(request):


    return render(request,"order.html")

