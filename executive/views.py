from django.shortcuts import render, redirect
from users.models import DeliveryInfo
from django.http import HttpResponse
from executive import forms
from users import forms as user_form
from accounts.decorators import executive_required
from executive.models import ExecutiveInfo
from django.contrib.auth.decorators import login_required
from accounts.models import User, order_id_count
import datetime


# view function for executives
@executive_required
def executive_user(request):
    orders = DeliveryInfo.objects.all().order_by('-date')
    # username = orders.username
    # phone = User.objects.get(username = username).phone
    return render(request, 'executive/executive_view.html', {'orders': orders})

@executive_required
def order_detail(request, id):
    # return HttpResponse(id)
    # global exec_read
    # exec_read = True
    # global uid
    order = DeliveryInfo.objects.get(id=id)
    order.exec_read = True
    order.is_seen = True
    order.user_read = False
    if request.method == 'POST':
        instance = ExecutiveInfo(executive=request.user)
        instance.customer = order.user
        instance.Locationlat = 0
        instance.Locationlong = 0
        instance.live_location = " "
        instance.executive = request.user
        instance.order_id = id
        print(instance.order_id)
        instance.save()
        return redirect('executive:executive_location')
    order.save()

    # global user_read
    # user_read = False
    return render(request, 'executive/confirm.html', {'order':order})

@executive_required
def user_confirmation(request):
    executive = ExecutiveInfo.objects.get(executive=request.user)
    id = executive.order_id
    print(id)
    query = DeliveryInfo.objects.get(id=id)
    if query.is_canceled:
        canceled_text = 'The request has been canceled by the user for some reason!!'
        return render(request, 'executive/confirm3.html', {'canceled_text': canceled_text})
    else:
        if query.user_read:
            user_read = query.user_read
            query.is_completed = True
            query.save()
            order = DeliveryInfo.objects.get(id=id)
            exec_coming = ExecutiveInfo.objects.get(customer=executive.customer)
            customer = User.objects.get(username = str(order.user))
            customer_phone = customer.phone
            user_agree_text = 'Congo!!! Customer is agreed on the amount..'
            return render(request, 'executive/confirm3.html', {'user_agree_text': user_agree_text, 'order': order, 'exec_coming': exec_coming, 'user_read': user_read, 'customer_phone': customer_phone})
        else:
            executive_wait_text = 'Please wait while user confirms the price and time.!!'
            return render(request, 'executive/confirm3.html', {'executive_wait_text':executive_wait_text})

@executive_required
def get_executivelocation(request):
    if request.method == 'POST':
        form = forms.GetExec_Location(request.POST)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.executive = request.user
            executive = ExecutiveInfo.objects.get(executive=request.user)
            id = executive.order_id
            instance.order_id = id
            instance.customer = executive.customer
            query = DeliveryInfo.objects.get(id=id)
            query.amount = instance.Amount
            query.duration_exec_pick = instance.Duration
            query.duration_pick_drop = instance.Duration_pick_drop
            instance.save()
            query.is_confirmed = True
            query.save()
            # if uid != 0:
            #     query = DeliveryInfo.objects.get(id=uid)
            #     query.is_completed = True
            #     query.save()
            # else:
            #     print("is zero", id)
            return redirect('executive:user_confirmation')


    else:
        form = forms.GetExec_Location()
        executive = ExecutiveInfo.objects.get(executive=request.user)
        id = executive.order_id
        order = DeliveryInfo.objects.get(id=id) # PROBLEM ARISES HERE BLOODY SHIT...!!!!
    return render(request, 'executive/confirm2.html', {'form':form, 'order':order})

# view functions for users

@login_required(login_url="/accounts/login/")
def get_pickupdrop(request):
    if request.method == 'POST':
        form = user_form.GetPickupDrop(request.POST)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.user = request.user

            count = order_id_count.objects.get(id=1)
            count.count_id = count.count_id + 1
            # instance.id = request.user.id
            instance.id = count.count_id
            now = datetime.datetime.now()
            instance.order_time = now.strftime("%H:%M")
            instance.date = now.strftime("%Y-%m-%d")
            # global is_confirmed
            # is_confirmed = False
            instance.save()
            query = User.objects.get(username=request.user)
            query.recent_order_id = count.count_id
            count.save()
            query.save()
            # query =  DeliveryInfo.objects.get(user=request.user).order_by('-id')[0]
            # query.is_confirmed = False
            # query.save()
            return redirect('users:delivery_details')

    else:
        form = user_form.GetPickupDrop()
    return render(request, 'users/pickup_drop_details.html',{'form':form})


@login_required(login_url="/accounts/login/")
def delivery_details(request):
    print(request.user.recent_order_id)
    query = DeliveryInfo.objects.get(id = request.user.recent_order_id)
    is_confirmed = query.is_confirmed
    # will have to write an if condition to see if the order is confirmed by executive or not
    print(is_confirmed)
    if is_confirmed is True:
        exec_coming = ExecutiveInfo.objects.get(customer=request.user)
        # exec_username = exec_coming.executive
        # exec_details = User.objects.get(username = exec_username)
        exec_read = query.exec_read
        # global user_read
        # user_read = True
        return render(request, 'users/delivery_details.html', {'exec_coming':exec_coming, 'exec_read':exec_read})
    else:
        wait_text = 'Please Wait till our executive give confirmation!'
        query = DeliveryInfo.objects.get(id=request.user.recent_order_id)
        query.is_confirmed = False
        return render(request, 'users/delivery_details.html', {'wait_text':wait_text})

@login_required(login_url="/accounts/login/")
def final_confirmation(request):
    query = DeliveryInfo.objects.get(id = request.user.recent_order_id)
    query.user_read = True
    query.save()
    exec_coming = ExecutiveInfo.objects.get(customer=request.user)
    exec_username = exec_coming.executive
    exec_details = User.objects.get(username = exec_username)
    return render(request, 'users/final_confirmation.html', {'exec_coming':exec_coming, 'exec_details':exec_details})

@login_required(login_url="/accounts/login/")
def order_cancel(request):
    query = DeliveryInfo.objects.get(id=request.user.recent_order_id)
    query.is_canceled = True;
    query.save()
    return redirect('users:normal_user')
