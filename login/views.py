from .forms import UserCreationForm, UserLoginForm, UserEditForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import auth


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        f = UserLoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect("/form/")

    else:
        f = UserLoginForm()

    return render(request, 'login.html', {'form': f})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


def form(request):
    return render(request, 'form.html')


def edit_form(request):
        if request.method == 'POST':
            f = UserEditForm(request.POST, request.FILES, instance=request.user)
            if f.is_valid():
                f.save()
                return HttpResponseRedirect("/form/")
        else:
            f = UserEditForm()
        return render(request, 'edit.html', {'form': f})


def register(request):
        if request.method == 'POST':
            f = UserCreationForm(request.POST)
            if f.is_valid():
                f.save()
                return HttpResponseRedirect("/login/")

        else:
            f = UserCreationForm()

        return render(request, 'register.html', {'form': f})

