from django.contrib import admin
from .models import Post, Comment


class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ("date_posted",)
    search_fields = ['title', 'content', 'author']

admin.site.register(Post, AdminPost)


class AdminComment(admin.ModelAdmin):
    list_display = ('post_id', 'author', 'date_posted', 'comment')
    list_filter = ("date_posted", 'post_id', 'author', 'comment')
    search_fields = ['post_id', 'comment', 'author']

admin.site.register(Comment, AdminComment)