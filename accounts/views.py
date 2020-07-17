from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import datetime
from django.db import models
from accounts.forms import ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from accounts.models import Profile, User_Account
from django.contrib.auth.models import Group
from application.models import Project

from django.contrib.auth.decorators import login_required
from application.decorators import user_is_in_project, user_is_admin_in_project

# Create your views here.


@login_required(login_url='account_login')
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url='account_login')
@user_is_admin_in_project
def add_user_project_view(request, slug):  
    reference = get_object_or_404(Project, project_url=slug)
    proj_name = reference.project_name.replace(" ", "_")
    groups = Group.objects.filter(name__startswith = proj_name)
    email = ''
    user_group = groups
    if request.method == 'POST' :
        email = request.POST.get('email').lower()
        user_group = request.POST.get('user_group')
        if User_Account.objects.filter(email = email):
            user = User_Account.objects.get(email = email)
            group_name=proj_name+'_'+user_group
            if group_name in user.groups.all(): 
                messages.error(request, "User is already in group")
            else:
                group = Group.objects.get(name = group_name)
                user.groups.add(group)
                return redirect('project_detail', slug) 
        else:
            messages.error(request, "Non-Existent E-mail")       
    context = {
        'project_url' : reference.project_url,
        'project' : reference.project_name,
        'user_group' : user_group,
        'email' : email
    }
    return render(request, "account/add_user_project.html", context)



@login_required(login_url='account_login')
@user_is_admin_in_project
def delete_user_project_view(request, slug, pk_email):
    reference = get_object_or_404(Project, project_url=slug)
    proj_name = reference.project_name.replace(" ", "_")
    user = get_object_or_404(User_Account, email = pk_email)
    if request.method == 'POST' :
        groups = Group.objects.filter(name__startswith = proj_name)
        for i in groups:
            user.groups.remove(i)
        return redirect('project_detail', slug) 
    context = {
        'project_url' : reference.project_url,
        'project' : reference.project_name,
        'email' : user.email,
    }
    return render(request, "account/delete_user_project.html", context)