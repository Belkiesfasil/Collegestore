from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Department, Course
from django.shortcuts import render, get_object_or_404, redirect
from django.core import serializers
import json


# Create your views here.

def getdata(request):
    template_name = 'dropdown.html'
    deptcontext = Department.objects.all()
    coursecontext = Course.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        date = request.POST.get('date', '')
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists")
                return redirect('dropdownapp:getdata')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('dropdownapp:getdata')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('loginapp:order')
                print("user registered")

        else:
            messages.info(request, "password not matching")
            return redirect('dropdownapp:getdata')

        return redirect('loginapp:order')

    return render(request, template_name, {'Department': deptcontext, 'Course': coursecontext})