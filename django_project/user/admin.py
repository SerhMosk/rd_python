from django.contrib import admin

# Register your models here.
from user.models import User

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'password',
        'first_name',
        'last_name',
        'age',
        'date_joined',
        'last_login',
        'is_active',
        'is_staff',
        'is_superuser',
    )
