from django.contrib import admin
from .models import *
# Register your models here.


class BookInline(admin.TabularInline):

    model = Book


class BookInstanceInline(admin.TabularInline):

    model = BookInstance


class AuthorAdmin(admin.ModelAdmin):

    list_display = ['last_name', 'first_name']
    fields = ['first_name', 'last_name', ('birth_day', 'die_day')]
    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'display_genre']
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):

    list_display = ['id', 'book', 'status', 'due_back']
    list_filter = ['status', 'due_back']
    fieldsets = (
        ('Kode', {
            'fields': ('book', 'inprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
