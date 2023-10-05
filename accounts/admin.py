from django.contrib.auth.admin import UserAdmin
from .models import Custom_User,Userprofile
from django.contrib  import admin

class CustomUserAdmin(UserAdmin):
     list_display=('email','first_name','last_name','username','role','is_active')
     ordering=['-date_joined']
     filter_horizontal=()
     list_filter=()
     fieldsets=()
     
     
admin.site.register(Custom_User,CustomUserAdmin)

admin.site.register(Userprofile)