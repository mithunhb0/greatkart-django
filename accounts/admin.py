from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile

# Custom password 
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
   
    # giving link to some fields
    list_display_links = ('email', 'first_name', 'last_name')
    
    # read only fields
    readonly_fields = ('last_login', 'date_joined')
    
    # order the fields
    ordering = ('-date_joined',)

    # read only password
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile)