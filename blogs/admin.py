from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'content', "updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    
    prepopulated_fields = {'slug': ('title',)}  #otomatis isi slug dari name
admin.site.register(Blog, BlogAdmin)