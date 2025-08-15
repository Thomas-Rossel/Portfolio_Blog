from django.contrib import admin
from .models import Post, Comment, Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted']
    list_filter = ['date_posted', 'author']
    search_fields = ['title', 'content']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'date_posted']
    list_filter = ['date_posted', 'author']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']