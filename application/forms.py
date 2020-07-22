from django.forms import ModelForm, Textarea, TextInput
from django import forms
from crispy_forms.helper import FormHelper
from application.models import Post, Project, Note
from django.utils.translation import gettext_lazy as _

#import magic
#https://stackoverflow.com/questions/20272579/django-validate-file-type-of-uploaded-file

from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat


class Post_Submission_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title','post_details','post_image_1','post_attachment')

        labels = {
            'post_title': _('Post Title'),
            'post_details': _('Post Text'),
            'post_image_1': _('Post Photo'),
            'post_attachment': _('Post Attachment'),
        }
        widgets = {
            'post_title': TextInput(attrs={'size': 30}),
            'post_details': Textarea(attrs={'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post' # get or post


class Note_Submission_Form(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('note_title','note_details')
        
        labels = {
            'note_title': _('Note Title'),
            'note_details': _('Note Text'),
        }
        widgets = {
            'note_title': TextInput(attrs={'size': 30}),
            'note_details': Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post' # get or post


class Project_Creation_Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name','project_active','project_intro','project_start_date','project_end_date')

        widgets = {
            'project_name': TextInput(attrs={'size': 30}),
            'project_intro': Textarea(attrs={'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post' # get or post