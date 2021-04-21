from django.contrib import admin
from .models import PostDescription, Post, AboutMe, Comments, HomeImages
# Register your models here.

admin.site.register(HomeImages)
admin.site.register(Post)
admin.site.register(PostDescription)
admin.site.register(AboutMe)
admin.site.register(Comments)