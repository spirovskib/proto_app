from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User_Account, Profile
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User_Account
#         fields = ['email','password1','password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'user_profile_url', 'user_bio', 'consent_marketing_notifications', 'private_profile']
        labels = {
            'name': _('Your Full Name'),
            'user_profile_url': _('Your Public Profile URL: https://ako.beyondmachines.net/profile/'),
            'consent_marketing_notifications': _('I Agree to Receiving Marketing Messages from BeyondMachines'),
            'user_bio': _('Your Brief Biography - 2000 characters max.'),
        }
        widgets = {
            'user_bio': Textarea(attrs={'rows': 10}),
        }
