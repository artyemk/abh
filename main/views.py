from django.shortcuts import render, redirect, HttpResponse
import logging
from django.utils import timezone

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
    return render(request, "index.html")

def lk(request):
    return render(request, "lk.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, "index.html")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

