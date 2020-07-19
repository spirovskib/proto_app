from application.forms import Post_Submission_Form, Project_Creation_Form, Note_Submission_Form
from application.models import Post, Project, Note
from django.shortcuts import render, get_object_or_404, redirect
from settings.constants import MAX_RESIZE_WIDTH, MAX_RESIZE_HEIGHT
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from application.decorators import user_is_in_project
from accounts.models import User_Account, Profile

from PIL import Image
import io

#this import is needed to create the groups of permissions
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
#this import is needed to create the groups of permissions



# Create your views here.

### START Custom HTML error handlers for nicer error messages
def err_handler403(request, exception):
    return render(request, 'errors/403.html', status=403)

def err_handler404(request, exception):
    return render(request, 'errors/404.html', status=404)
### END Custom HTML error handlers for nicer error messages


def home_view(request, *args, **kwargs):  
    #return HttpResponse("<h1>Home Page</h1>") 
    projects = Project.objects.filter(project_active=True).order_by('-project_start_date')
    notes = Note.objects.all().order_by('-note_published_date')
    context = {
        'projects' : projects,
        'notes' : notes
    }
    return render(request, "home.html", context)

@login_required(login_url='account_login')
@user_is_in_project
def view_post_detail(request, slug):  
    post = Post.objects.get(post_url = slug)
    #return HttpResponse("<h1>Home Page</h1>") 
    context = {
        'post':post,
    }
    return render(request, "post/view_post.html", context)

@login_required(login_url='account_login')
@user_is_in_project
def new_post_view(request, slug):
    reference = get_object_or_404(Project, project_url=slug)
    if request.method == 'POST' : 
        submission_form = Post_Submission_Form(request.POST,request.FILES)
        if submission_form.is_valid():
            instance = submission_form.save(commit=False) #this seems to work for saving the user... 
            #resizing of input image
            if instance.post_image_1:
                image = Image.open(instance.post_image_1)
                w,h=image.size
                if w > MAX_RESIZE_WIDTH or h > MAX_RESIZE_HEIGHT:
                    ratio = w/h
                    if ratio > 1:
                        resize_height = int(MAX_RESIZE_WIDTH/ratio)
                        resize_width = MAX_RESIZE_WIDTH
                    else:
                        resize_width = int(ratio/MAX_RESIZE_HEIGHT)
                        resize_height = MAX_RESIZE_HEIGHT
                    image = image.resize((resize_width, resize_height), Image.ANTIALIAS)
                    image_file = io.BytesIO()
                    image.save(image_file, 'JPEG', quality=95)
                    instance.post_image_1.file=image_file
            #resizing of input image
            instance.project = reference
            instance.save()
            url_link = instance.post_url
            return redirect('view_post', url_link) 
    else:   
        submission_form = Post_Submission_Form()
    context = {
        'reference' : reference,
        'submission_form' : submission_form,
    }
    return render(request, "post/new_post.html", context)

@login_required(login_url='account_login')
def view_note_detail(request, slug):  
    post = get_object_or_404(Note, note_url=slug)
    #return HttpResponse("<h1>Home Page</h1>") 
    context = {
        'post':post,
    }
    return render(request, "view_note.html", context)

@login_required(login_url='account_login')
def new_note_view(request, *args, **kwargs):
    if request.method == 'POST' : 
        note_form = Note_Submission_Form(request.POST)
        if note_form.is_valid():
            instance = note_form.save(commit=False)
            instance.note_author = request.user
            instance.save()
            url_link = instance.note_url
            return redirect('view_note', url_link) 
    else:   
        note_form = Note_Submission_Form()
    context = {
        'note_form' : note_form,
    }
    return render(request, "new_note.html", context)

@login_required(login_url='account_login')
def new_project_view(request, *args, **kwargs): 
    if request.user.profile.project_credits > 25: ### Check if user has credit to create project
        if request.method == 'POST' : 
            project_form = Project_Creation_Form(request.POST)
            if project_form.is_valid():
                instance = project_form.save(commit=False)
                proj_name = project_form.cleaned_data.get('project_name').replace(" ", "_")

                ### START adding permissions to group
                ct = ContentType.objects.get_for_model(Project)
                admin_group, created = Group.objects.get_or_create(name= proj_name+'_'+'admin')
                user_group, created = Group.objects.get_or_create(name= proj_name+'_'+'user')

                permission = Permission.objects.create(codename=proj_name+'_'+'can_list_posts', name='List Posts', content_type=ct)
                admin_group.permissions.add(permission)
                user_group.permissions.add(permission)

                permission = Permission.objects.create(codename=proj_name+'_'+'can_view_post', name='View Post Details', content_type=ct)
                admin_group.permissions.add(permission)
                user_group.permissions.add(permission)

                permission = Permission.objects.create(codename=proj_name+'_'+'can_create_post', name='Create Post', content_type=ct)
                admin_group.permissions.add(permission)
                user_group.permissions.add(permission)

                permission = Permission.objects.create(codename=proj_name+'_'+'can_list_users', name='List Project Users', content_type=ct)
                admin_group.permissions.add(permission)
                user_group.permissions.add(permission)

                permission = Permission.objects.create(codename=proj_name+'_'+'can_invite_users', name='Invite Project Users', content_type=ct)
                admin_group.permissions.add(permission)

                permission = Permission.objects.create(codename=proj_name+'_'+'can_manage_project', name='Manage Project', content_type=ct)
                admin_group.permissions.add(permission)
                ### END adding permissions to group

                ### START add first admin to project
                request.user.groups.add(admin_group)
                ### END add first admin to project

                instance.save()

                ### START decrease credit for new project
                profile = Profile.objects.get(user=request.user)
                profile.project_credits -= 25
                profile.save()
                ### END decrease credit for new project

                url_link = instance.project_url
                return redirect('project_detail', url_link) 
        else:   
            project_form = Project_Creation_Form()
        context = {
            'project_form' : project_form,
        }
        return render(request, "project/new_project.html", context)
    else:
        return render(request, "errors/no_credit.html", {})



@login_required(login_url='account_login')
@user_is_in_project
def project_detail_view(request, slug):  
    project = get_object_or_404(Project, project_url=slug)
    posts = Post.objects.filter(project__project_url = slug)
    proj_name = project.project_name.replace(" ", "_")
    groups = Group.objects.filter(name__startswith = proj_name)
    users_in_group=[]
    for i in groups:
        users_in_group.append(Group.objects.get(name = i.name).user_set.all())
    context = {
        'project':project,
        'posts':posts,
        'users_in_group':users_in_group
    }
    return render(request, "project/view_project.html", context)
