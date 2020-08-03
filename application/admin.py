from django.contrib import admin

# Register your models here.
from application.models import Post, Project, Note


#START: this is the view for the Challenge model area in admin
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('post_title','post_details','post_image_1','post_attachment')
admin.site.register(Post,PostModelAdmin)


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('project_name','project_code','project_active','project_start_date','project_end_date')
admin.site.register(Project,ProjectModelAdmin)

class NoteModelAdmin(admin.ModelAdmin):
    list_display = ('note_title','note_author')
admin.site.register(Note,NoteModelAdmin)