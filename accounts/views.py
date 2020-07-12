from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.db import models
from accounts.forms import ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from accounts.models import Profile, User_Account

# Create your views here.


# def register_view(request, *args, **kwargs):  # python specific http request and arguments: *args **kwargs. Using request.user is good for auth
#     #return HttpResponse("<h1>Register Page</h1>") 
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == 'POST' : 
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user_email = form.cleaned_data.get('email')
#                 user_password = form.cleaned_data.get('password1')
#                 account = authenticate(email=user_email, password=user_password)
#                 login(request,account)
#                 return redirect('home')
#             else:
#                 context= {'form':form}
#         else: #get request here
#             form = CreateUserForm()
#             context = {'form':form}
#         return render(request, "accounts/signup.html", context)


# def login_view(request, *args, **kwargs):  # python specific http request and arguments: *args **kwargs. Using request.user is good for auth
#     #return HttpResponse("<h1>Login Page</h1>") 
#     #next=request.GET.get('next')
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == 'POST':
#             user_email = request.POST.get('email')
#             user_password = request.POST.get('password')

#             account = authenticate(email=user_email, password=user_password)

#             if account is not None:
#                 login(request, account)
#                 return redirect('home')
#             else:
#                 messages.info(request,"Incorrect Email or Password")

#         context = {}
#         return render(request, "accounts/login.html", context)


@login_required(login_url='account_login')
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url='account_login')
def profile_view(request, *args, **kwargs): 
    profile = request.user.profile
#   What this does is get all the dates and then it gets the count of primary keys (aka number of rows) for each date where the filter matches.
    context = {
        'profile':profile,
    }
    return render(request, "account/profile.html", context) 


@login_required(login_url='login')
def profile_user_view(request, slug):  # python specific http request and arguments: *args **kwargs. Using request.user is good for auth
    profile = Profile.objects.get(user_profile_url = slug)

#   fixing the missing dates in the queryset by add    
    if profile.private_profile:
        profile = "The user has not made their profile visible"

    context = {
        'profile':profile,
        #'my_showcase_visits': newlist, #second graph data
        #'topic_visits': topic_visits, #third graph data
    }
    return render(request, "account/user_profile.html", context) 
