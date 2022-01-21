from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ('title',)
    ordering = ['title']
    search_fields = ['title']

admin.site.register(Blog, BlogAdmin)