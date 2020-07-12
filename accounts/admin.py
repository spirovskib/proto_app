from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User_Account, Profile

# Register your models here.

#START: this is the view for the custom user accounts. Defines what is displayed, what can be searched and what fields cannot be modified in admin
class AccountAdmin(UserAdmin): 
    list_display = ('email', 'date_joined', 'last_login', "is_admin", "is_staff")
    search_fields = ('email','is_admin')
    readonly_fields = ('email','date_joined', 'last_login')
    ordering = ('email','is_admin')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User_Account, AccountAdmin)
#END: this is the view for the custom user accounts


#START: this is the view for the custom user profile
class ProfileAdmin(admin.ModelAdmin): 
    list_display = ('name','private_profile')

admin.site.register(Profile, ProfileAdmin)
#END: this is the view for the custom user profile

