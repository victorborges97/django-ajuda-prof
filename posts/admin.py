from django.contrib import admin
from .models import Post, Comment, Categoria

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Comment)