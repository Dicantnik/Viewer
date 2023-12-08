from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib import messages


def auth_login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('rooms:main') 
            else:
                 messages.success(request, 'Something went wrong')
                 return redirect('users:login')   
    else:
         return render(request, 'registration/login.html', {})

def register(request):
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('rooms:main')
        else:
             messages.success(request,'Something went wrong')
    context = {'form': form}
    return render(request, 'registration/registration.html', context)

def logoutus(request):
    return redirect('rooms:main') 