from django.contrib import admin
from .models import Post
from .forms import PostCreateFormAdmin

class PostCreateAdmin(admin.ModelAdmin):
    form = PostCreateFormAdmin
    list_display = ["title", "approved", "views"]
    list_editable = ["approved"]
    list_filter = ["approved"]

admin.site.register(Post,PostCreateAdmin)