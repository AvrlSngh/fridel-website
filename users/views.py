from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required
from executive.models import ExecutiveInfo
from users.models import DeliveryInfo
from accounts.models import User, order_id_count
from executive import views
import datetime

customer = " "

@login_required(login_url="/accounts/login/")
def normal_user(request):
    customer = str(request.user)
    recent_order = DeliveryInfo.objects.filter(user=request.user)
    recent_order = recent_order[len(recent_order)-1]
    print(recent_order)
    return render(request, 'users/normal_user.html', {'customer':customer, 'recent_order':recent_order})


@login_required(login_url="/accounts/login/")
def orders_history(request):
    orders = DeliveryInfo.objects.filter(user = request.user)
    return render(request, 'users/orders_history.html', {'orders':orders})

@login_required(login_url="/accounts/login/")
def other_task(request):
    if request.method == 'POST':
        form = forms.OtherTasksForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user

            count = order_id_count.objects.get(id=1)
            count.count_id = count.count_id + 1

            instance.id = count.count_id
            now = datetime.datetime.now()
            instance.order_time = now.strftime("%H:%M")
            instance.date = now.strftime("%Y-%m-%d")
            instance.save()
            query = User.objects.get(username=request.user)
            query.recent_order_id = count.count_id
            count.save()
            query.save()
            return redirect('users:delivery_details')
    else:
        form = forms.OtherTasksForm()
    return render(request, 'users/other_tasks.html', {'form':form})
