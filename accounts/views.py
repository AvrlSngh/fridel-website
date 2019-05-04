from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from .forms import SignUpForm
from .models import User
from authy.api import AuthyApiClient

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)

            if user.is_executive:
                if user.is_executive:
                    return redirect('executive:executive_user')
                elif 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('executive:executive_user')

            else:
                return redirect('users:normal_user')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login_view.html', {'form':form})


class signup_view(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'accounts/signup_view.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'NormalUser'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        # authy_api = AuthyApiClient('bRswEbgitGVmzXWTvhnbEvuJkE21rJj1')
        # phone_number = self.request.POST.get("phone")
        # request = authy_api.phones.verification_start(phone_number, 91, via='sms', locale='en')
        # print (request.content)
        # verification_code = self.request.POST.get("verify_code")
        user = form.save()
        login(self.request, user)
        return redirect('accounts:verify_phone')
# NOT WORKED YET!!!!!!!
        # if verification_code != "" :
        #     check = authy_api.phones.verification_check(phone_number, 91, verification_code)
        #     if check.ok():
        #         user = form.save()
        #         login(self.request, user)
        #         return redirect('users:normal_user')
        #     else:
        #         error_message = "Phone number is not verified"
        #         return render(self.request, 'accounts/signup_view.html', {'error_message':error_message})

# and finally i fucked it ;-\) whoooohoooo...!!!
def verify_phone(request):
    authy_api = AuthyApiClient('bRswEbgitGVmzXWTvhnbEvuJkE21rJj1')
    phone_number = User.objects.get(username = request.user).phone
    verification_code = request.POST.get("verify_phone")
    check = authy_api.phones.verification_check(phone_number, 91, verification_code)
    print(phone_number)
    error_text = ""
    print(verification_code)
    if not check.ok():
        req = authy_api.phones.verification_start(phone_number, 91, via='sms', locale='en')
        print (req.content)
        print(check.ok())
    elif check.ok():
        request.user.is_user_verified = True
        request.user.save()
        return redirect('users:normal_user')
    if verification_code != " " and not check.ok():
        error_text = "OTP not sent. Change the number!"
        return render(request, 'users/normal_user.html', {'error_text':error_text})
    return render(request, 'accounts/verify_phone.html', {'phone_number': phone_number})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
