from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required
from executive.models import ExecutiveInfo
from users.models import DeliveryInfo
from accounts.models import User
from executive import views

customer = " "

@login_required(login_url="/accounts/login/")
def normal_user(request):
    customer = str(request.user)
    return render(request, 'users/normal_user.html', {'customer':customer})


@login_required(login_url="/accounts/login/")
def orders_history(request):
    orders = DeliveryInfo.objects.filter(user = request.user)
    return render(request, 'users/orders_history.html', {'orders':orders})
