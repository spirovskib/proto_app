from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_list_or_404, get_object_or_404


from application.models import Project, Post


### START the project access permissions decorator 
### example use:     @user_is_in_project
def user_is_in_project(function):
    def wrap(request, *args, **kwargs):
        #reference = get_object_or_404(Project, project_url=kwargs['slug'])
        if Project.objects.filter(project_url = kwargs['slug']):
            project = Project.objects.get(project_url = kwargs['slug'])
        else:
            if Post.objects.filter(post_url = kwargs['slug']):
                post = Post.objects.get(post_url = kwargs['slug'])
                project = post.project
        #proj_name = project.project_name.replace(" ", "_")
        groups = Group.objects.filter(name__startswith = project.project_code)
        group_list = []
        for i in groups:
            group_list.append(i.name)
        if request.user.groups.filter(name__in=group_list):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
### END the project access permissions decorator 


def user_is_admin_in_project(function):
    def wrap(request, *args, **kwargs):
        #reference = get_object_or_404(Project, project_url=kwargs['slug'])
        if Project.objects.filter(project_url = kwargs['slug']):
            project = Project.objects.get(project_url = kwargs['slug'])
        else:
            if Post.objects.filter(post_url = kwargs['slug']):
                post = Post.objects.get(post_url = kwargs['slug'])
                project = post.project
        group_name = project.project_code+'_'+'admin'
        if request.user.groups.filter(name = group_name):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
### END the project access permissions decorator 