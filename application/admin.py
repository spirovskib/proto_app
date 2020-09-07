from django.contrib import admin
from application.models import Post, Project, Note

# Register your models here.
# EXAMPLE: this is the view for the Post model area in admin


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_details', 'challenge_published_date', 'challenge_active')


admin.site.register(Post, PostModelAdmin)


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_code', 'project_active', 'project_start_date', 'project_end_date')


admin.site.register(Project, ProjectModelAdmin)


class NoteModelAdmin(admin.ModelAdmin):
    list_display = ('note_title', 'note_author')


admin.site.register(Note, NoteModelAdmin)
