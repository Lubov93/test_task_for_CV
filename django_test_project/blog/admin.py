from django.contrib import admin
from .models import Post, Comment


admin.site.site_header = "Blog Admin"
admin.site.site_title = "PythonBlog"

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','date_posted', 'image']
    list_filter = ('author','date_posted')

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content','post','author','date']
    list_filter = ('author','date','post__title')


admin.site.register(Post,PostAdmin)

admin.site.register(Comment,CommentAdmin)