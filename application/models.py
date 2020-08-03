from django.db import models
from datetime import date, datetime 
from slugify import slugify
import random
import string
from settings.validators import validate_file_type_size
from accounts.models import User_Account
from ckeditor.fields import RichTextField



# Create your models here.



# This link is useful for the use of magic for validation
# https://stackoverflow.com/questions/20272579/django-validate-file-type-of-uploaded-file
# This link is useful for the use of magic for validation



class Project(models.Model):
    project_name = models.CharField(max_length=70, blank=False, null=False, unique = True)
    project_code = models.CharField(max_length=70, blank=True, null=True, unique = True)
    project_active = models.BooleanField(default=True, null=False) #null=True, default=True
    # s: ModelChoiceField for the project type - learn how!
    project_url = models.SlugField(max_length=100, blank=True, null=True) #the slug text for the url
    project_intro = RichTextField(blank=False, null=False) #rich text version from ckedirot. PLEASE_NOTE That this field is NOT inherited from models
    project_start_date = models.DateField(blank=True, null=False, default=date.today)
    project_end_date = models.DateField(blank=True, null=True)

    class Meta:       
        permissions = ( 
            ("can_list_posts", "List Posts"),  #projects
            ("can_view_post", "View Post Details"), 
            ("can_create_post", "Create Post"), 
            ("can_invite_users", "Invite Project Users"), 
            ("can_list_users", "List Project Users"), 
            ("can_manage_project", "Manage Project"), 
        )

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs): # the autogeneration of the slug for the post
        if not self.project_code:
            self.project_code = str(self.project_name.replace(" ", "_"))
        if not self.project_url:
            self.project_url = slugify(self.project_name+'-'+str(self.project_start_date)+'-'+str(random.choices(string.ascii_uppercase + string.digits, k=4)))
        super(Project, self).save(*args, **kwargs)



class Post(models.Model):
    project = models.ForeignKey(Project, blank=False, null=True, on_delete=models.SET_NULL)
    post_title = models.CharField(max_length=70, blank=False, null=False)
    post_active = models.BooleanField(default=True, null=False) #null=True, default=True
    post_url = models.SlugField(max_length=100, blank=True, null=True) #the slug text for the url
    post_details = RichTextField(blank=False, null=False) #rich text version from ckedirot. PLEASE_NOTE That this field is NOT inherited from models
    post_published_date = models.DateTimeField(blank=True, null=False, auto_now=True)
    post_image_1 = models.ImageField(blank=True, null=True, 
        upload_to="images/%Y/%m/%d/",max_length=255)
    post_attachment = models.FileField(blank=True, null=True, 
        upload_to="files/%Y/%m/%d/",max_length=255, validators=[validate_file_type_size])

    def __str__(self):
        return self.post_title

    def save(self, *args, **kwargs): # the autogeneration of the slug for the post
        if not self.post_url:
            self.post_url = slugify(self.post_title+'-'+str(self.post_published_date)+'-'+str(random.choices(string.ascii_uppercase + string.digits, k=4)))
        super(Post, self).save(*args, **kwargs)


class Note(models.Model):
    note_author = models.ForeignKey(User_Account,blank=False,null=True,on_delete=models.SET_NULL)
    note_title = models.CharField(max_length=70, blank=False, null=False)
    note_url = models.SlugField(max_length=100, blank=True, null=True) #the slug text for the url
    note_details = RichTextField(blank=False, null=False) #rich text version from ckedirot. PLEASE_NOTE That this field is NOT inherited from models
    note_published_date = models.DateTimeField(blank=True, null=False, auto_now=True)
  
    def __str__(self):
        return self.note_title

    def save(self, *args, **kwargs): # the autogeneration of the slug for the post
        if not self.note_url:
            self.note_url = slugify(self.note_title+'-'+str(self.note_published_date)+'-'+str(random.choices(string.ascii_uppercase + string.digits, k=4)))
        super(Note, self).save(*args, **kwargs)
