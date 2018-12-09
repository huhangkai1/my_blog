"""article URL Configuration
"""
from django.urls import path
from . import views

# 正在部署的app名称
app_name = 'article'

# 存放映射关系的列表
urlpatterns = [
    # 将url映射到试图
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>', views.article_detail, name='article_detail'),
]
