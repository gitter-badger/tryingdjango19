from django.contrib import admin

# Register your models here.
# from posts.models import Post
from .models import Post

admin.site.register(Post)