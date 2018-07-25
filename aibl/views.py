from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def terms(request):
    return render(request, 't&c.html')
