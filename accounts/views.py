from django.shortcuts import render,redirect
from .forms import SignupForm
from .models import Account
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/index.html', {'error': 'Please try another username'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'], password=request.POST['password1'])
                auth.login(request, user)
                return render(request,'accounts/success.html')
        else:
            return render(request, 'accounts/index.html', {'error': "Passwords didn't match"})

    else:
        return render(request, 'accounts/index.html')