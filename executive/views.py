from django.shortcuts import render, redirect
from users.models import DeliveryInfo
from django.http import HttpResponse
from executive import forms
from users import forms as user_form
from accounts.decorators import executive_required
from executive.models import ExecutiveInfo
from django.contrib.auth.decorators import login_required
from accounts.models import User, order_id_count
from webpush import send_user_notification
import datetime
from django.conf import settings

# ============================================================================================================================


                                                    # EXECUTIVE USER

@executive_required
def executive_user(request):
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    user = request.user
    orders = DeliveryInfo.objects.all().order_by('-date')
    return render(request, 'executive/executive_view.html', {'orders': orders, user: user, 'vapid_key': vapid_key})



# ============================================================================================================================

                                                    #GET EXECUTIVE LOCATION

@executive_required
def get_executivelocation(request):
    if request.method == 'POST':
        form = forms.GetExec_Location(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.executive = request.user

            # ------------------------------------------------------
            info = ExecutiveInfo.objects.filter(executive=request.user)
            executive = info[len(info)-1]
            # ------------------------------------------------------

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
            return redirect('executive:user_confirmation')


    else:
        form = forms.GetExec_Location()

        # ------------------------------------------------------
        info = ExecutiveInfo.objects.filter(executive=request.user)
        executive = info[len(info)-1]
        # ------------------------------------------------------

        id = executive.order_id
        order = DeliveryInfo.objects.get(id=id) # PROBLEM ARISES HERE BLOODY SHIT...!!!!
    if order.other_task:
        return render(request, 'executive/confirm_other.html', {'form':form, 'order':order})
    else:
        return render(request, 'executive/confirm2.html', {'form':form, 'order':order})


# ============================================================================================================================

                                                    # ORDER DETAIL

@executive_required
def order_detail(request, id):
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

    return render(request, 'executive/confirm.html', {'order':order})


# ============================================================================================================================

                                                    # USER CONFIRMATION

@executive_required
def user_confirmation(request):
    # ------------------------------------------------------
    info = ExecutiveInfo.objects.filter(executive=request.user)
    executive = info[len(info)-1]
    # ------------------------------------------------------

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

            # ------------------------------------------------------
            info = ExecutiveInfo.objects.filter(customer=executive.customer)
            exec_coming = info[len(info)-1]
            # ------------------------------------------------------

            customer = User.objects.get(username = str(order.user))
            customer_phone = customer.phone
            user_agree_text = 'Congo!!! Customer is agreed on the amount..'
            return render(request, 'executive/confirm3.html', {'user_agree_text': user_agree_text, 'order': order, 'exec_coming': exec_coming, 'user_read': user_read, 'customer_phone': customer_phone})
        else:
            executive_wait_text = 'Please wait while user confirms the price and time.!!'
            return render(request, 'executive/confirm3.html', {'executive_wait_text':executive_wait_text})


# ============================================================================================================================

                                                        # GET PIKCUP DROP
@login_required(login_url="/accounts/login/")
def get_pickupdrop(request):
    if request.method == 'POST':
        form = user_form.GetPickupDrop(request.POST)
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
        form = user_form.GetPickupDrop()
    return render(request, 'users/pickup_drop_details.html',{'form':form})


# ============================================================================================================================

                                                    # DELIVERY DETAILS

@login_required(login_url="/accounts/login/")
def delivery_details(request):
    print(request.user.recent_order_id)
    query = DeliveryInfo.objects.get(id = request.user.recent_order_id)
    is_confirmed = query.is_confirmed
    # will have to write an if condition to see if the order is confirmed by executive or not
    print(is_confirmed)
    if is_confirmed is True:

        # ------------------------------------------------------
        info = ExecutiveInfo.objects.filter(order_id=request.user.recent_order_id) # To store the query set in order to retrieve last element
        exec_coming = info[len(info)-1]
        # ------------------------------------------------------

        exec_read = query.exec_read
        return render(request, 'users/delivery_details.html', {'exec_coming':exec_coming, 'exec_read':exec_read})
    else:
        wait_text = 'Please Wait till our executive give confirmation!'
        query = DeliveryInfo.objects.get(id=request.user.recent_order_id)
        query.is_confirmed = False
        return render(request, 'users/delivery_details.html', {'wait_text':wait_text})


# ============================================================================================================================

                                                    # FINAL CONFIRMATION

@login_required(login_url="/accounts/login/")
def final_confirmation(request):
    query = DeliveryInfo.objects.get(id = request.user.recent_order_id)
    query.user_read = True
    is_other = False
    if query.other_task:
        is_other = True
    query.save()

    # ------------------------------------------------------
    info = ExecutiveInfo.objects.filter(customer=request.user)
    exec_coming = info[len(info)-1]
    # ------------------------------------------------------

    exec_username = exec_coming.executive
    exec_details = User.objects.get(username = exec_username)

    # checking the checkbox of offer_claimed when user got the details of executive
    request.user.offer_claimed = True
    request.user.save()

    return render(request, 'users/final_confirmation.html', {'exec_coming':exec_coming, 'exec_details':exec_details, 'is_other':is_other})


# ============================================================================================================================

                                                    # ORDER CANCEL

@login_required(login_url="/accounts/login/")
def order_cancel(request):
    query = DeliveryInfo.objects.get(id=request.user.recent_order_id)
    query.is_canceled = True;
    query.save()
    return redirect('users:normal_user')


# x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
