from django.contrib import admin

# Register your models here.
from purchase.models import Purchase

# admin.site.register(Purchase)


@admin.register(Purchase)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'book_id',
        'user_id',
        'created_at',
    )
