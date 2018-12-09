from django.contrib import admin
from . import models

# 注册ArticlePost加入到admin中
admin.site.register(models.ArticlePost)
