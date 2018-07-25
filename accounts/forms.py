from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.db import transaction
from .models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(max_length=254, help_text='Required a valid email address.')
    # phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')


    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
                    'username',
                    'email',
                    'phone',
                    'first_name',
                    'last_name',
                    'password1',
                    'password2',
                )

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_executive = False
        user.save()
        # normal_user = NormalUser.objects.create(user=user)
        # normal_user.first_name = self.cleaned_data['first_name']
        # normal_user.last_name = self.cleaned_data['last_name']
        return user
