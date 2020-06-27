from django.forms import ModelForm
from django import forms
from application.models import Post

#import magic
#https://stackoverflow.com/questions/20272579/django-validate-file-type-of-uploaded-file

from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat




class Post_Submission_Form(forms.ModelForm):
    # def clean_file(self):
    #     file = self.cleaned_data.get("post_attachment", False)
    #     filetype = magic.from_buffer(file.read())
    #     if not "XML" in filetype:
    #         raise ValidationError("File is not XML.")
    #     return file

    class Meta:
        model = Post
        fields = ('post_title','post_details','post_image_1','post_attachment')

