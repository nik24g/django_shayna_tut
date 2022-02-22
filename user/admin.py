from django.contrib import admin
from user.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('id', 'email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')

    fieldsets = (
        ("details", {
            "fields": (
                'email',
                'password',
                'username',
                'first_name',
                'last_name',
                'address',
                'image'
            ),
        }),
        ('permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')})
    )
    
    add_fieldsets = (
        (None, {
            "classes": ('wide',),
            "fields": (
                'email',
                'username',
                'first_name',
                'last_name',
                'image',
                'password1',
                'password2',
                'is_staff',
                'is_superuser',
                'is_active'
            ),
        }),
    )

    ordering = ('email',)
    

# admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Student)
admin.site.register(Employee)