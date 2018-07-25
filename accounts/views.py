from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from .forms import SignUpForm
from .models import User

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
        user = form.save()
        login(self.request, user)
        return redirect('users:normal_user')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
