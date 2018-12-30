"""article URL Configuration
"""
from django.urls import path
from . import views

# 正在部署的app名称
app_name = 'article'

# 存放映射关系的列表
urlpatterns = [
    # 文章主页
    path('article-list/', views.article_list, name='article_list'),
    # 文章详情页
    path('article-detail/<int:article_id>/', views.article_detail, name='article_detail'),
    # 写文章
    path('article-create/', views.article_create, name='article_create'),
    # 删除文章
    path('article-delete/<int:article_id>/', views.article_delete, name='article_delete'),
    # 编辑文章
    path('article-update/<int:article_id>/', views.article_update, name='article_update'),

    path('', views.article_list, name='article_detail'),

]
