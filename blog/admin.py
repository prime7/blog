from django.contrib import admin
from .models import Post
from .forms import PostCreateFormAdmin

class PostCreateAdmin(admin.ModelAdmin):
    form = PostCreateFormAdmin


admin.site.register(Post,PostCreateAdmin)