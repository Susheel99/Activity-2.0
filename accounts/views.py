from django.shortcuts import render,redirect
from .forms import SignupForm
from .models import Account
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Please try another username'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'], password=request.POST['password1'])
                user.save()
                # auth.login(request, user)
                return render(request,'homepage.html')
        else:
            return render(request, 'accounts/signup.html', {'error': "Passwords didn't match"})

    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, 'project/homepage.html')
        else:
            return render(request, 'accounts/login.html',{'error':"Invalid credentials"})

    return render(request, 'accounts/login.html')


def logout(request):
    auth_logout(request)
    return render(request, 'homepage.html')
