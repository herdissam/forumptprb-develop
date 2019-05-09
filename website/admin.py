from django.contrib import admin

# Register your models here.
from .models import Post
from .models import UserProfile

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["title","updated"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)

admin.site.register(UserProfile)