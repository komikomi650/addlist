from django.contrib import admin
from .models import Post, Category

# Register your models here.

#　管理サイトでmodels.pyで定義したものを操作できるようにする
admin.site.register(Post)
admin.site.register(Category)