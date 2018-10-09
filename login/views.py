from .forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html')

#TODO вход


def login(request):
    return render(request, 'login.html')


#TODO ВЫХОД
#TODO АНКЕТА
#TODO изменение анкеты

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = CustomUserCreationForm()

    return render(request, 'register.html', {'form': f})