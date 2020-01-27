from django.contrib import admin
from .models import Account

from django.contrib.auth.models import Group



class UserAdmin(admin.ModelAdmin):
    search_fields= ['email']
    ordering = ['email']
    list_display= ['email', 'is_admin']
    list_filter = ['is_staff', 'is_admin']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
# Register your models here.
admin.site.register(Account, UserAdmin)
# Unregister Group
admin.site.unregister(Group)