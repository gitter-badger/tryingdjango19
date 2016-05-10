from django.contrib import admin

# Register your models here.
# from posts.models import Post
from .models import Post

# connects Post model to the Admin
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post
        
# register the Post model
# admin.site.reigster(Post)
admin.site.register(Post, PostModelAdmin)