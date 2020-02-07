from django.contrib import admin

# Register your models here.
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["_unicode_",'title',"utimestamp","timestamp"]
    list_display_links=["utimestamp"]
    list_editable=["title"]
    list_filter = ['utimestamp','timestamp']
    search_fields=["title" , 'content']
    class meta:
        model = Post



admin.site.register(Post, PostAdmin)
