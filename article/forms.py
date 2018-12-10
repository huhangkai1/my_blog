# 引入表单类
from django import forms
# 引入文章模型
from .models import ArticlePost


# 写入文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title', 'body')
