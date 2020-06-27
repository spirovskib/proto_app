from django.contrib import admin

# Register your models here.
from application.models import Post


#START: this is the view for the Challenge model area in admin
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('post_title','post_details','post_image_1','post_attachment')
admin.site.register(Post,PostModelAdmin)