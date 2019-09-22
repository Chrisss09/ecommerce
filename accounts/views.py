from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    """Return HTML file"""
    return render(request, 'index.html')

@login_required
def logout(request):
    """Logs user out"""
    auth.logout(request)
    messages.success(request, "You have been successfully logged out")
    return redirect(reverse('index'))

def login(request):
    """Login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})

def register(request):
    """Registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account")
        
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'register.html', {'registration_form': registration_form})

def profile(request):
    """User Profile Page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'profile': user})