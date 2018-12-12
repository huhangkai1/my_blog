"""userprofile URL Configuration
"""
from django.urls import path
from . import views

# 正在部署的app名称
app_name = 'user'

# 存放映射关系的列表
urlpatterns = [
    # 登录页
    path('login/', views.user_login, name='login'),
    # 退出登录
    path('logout/', views.user_logout, name='logout'),
    # 用户注册
    path('register/', views.user_register, name='register'),

]
