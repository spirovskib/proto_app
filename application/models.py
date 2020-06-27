from django.db import models
from datetime import date 
from slugify import slugify
import random
import string
from application.validators import validate_file_type_size


# Create your models here.



# This link is useful for the use of magic for validation
# https://stackoverflow.com/questions/20272579/django-validate-file-type-of-uploaded-file
# This link is useful for the use of magic for validation


class Post(models.Model):
    post_title = models.CharField(max_length=70, blank=False, null=False)
    post_active = models.BooleanField(default=True, null=False) #null=True, default=True
    post_url = models.SlugField(max_length=100, blank=True, null=True) #the slug text for the url
    post_details = models.TextField(blank=False, null=False) #rich text version from ckedirot. PLEASE_NOTE That this field is NOT inherited from models
    post_published_date = models.DateField(blank=True, null=False, default=date.today)
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
