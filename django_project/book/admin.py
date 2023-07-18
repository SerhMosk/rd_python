from django.contrib import admin

# Register your models here.
from book.models import Book

# admin.site.register(Book)


@admin.register(Book)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'year',
        'price',
    )
