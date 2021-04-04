from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('login.html')
    return render(request, 'index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # checking user credentials
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            messages.success(request, "Wrong Credentials")
            return render(request, 'login.html')

    return render(request, 'login.html')

def signupUser(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.success(request, "Username has already been taken")
                return redirect('signup.html')
            elif User.objects.filter(email=email).exists():
                messages.success(request, "Try with another Email. Seems like anyone already have it!!!")
                return redirect('signup.html')
            else:    
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
                user.save()
                print("user created")
        else:
            messages.success(request, 'Password Not Matching!!!')
            return redirect('signup.html')
        return redirect("login.html")

    else:  
        return render(request, 'signup.html')

def logoutUser(request):
    logout(request)
    return redirect('login.html')
        
            
             
