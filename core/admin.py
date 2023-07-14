from django.contrib import admin
from .models import BookModel, AuthorModel
@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','publisher','language','pages','created', 'updated' ]

@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','about','created', 'updated']