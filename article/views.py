from django.shortcuts import render
from .models import ArticlePost
import markdown


# 博客主页
def article_list(request):
    # 取出所有文章
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html', context)


# 文章详情页
def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)

    # 将markdown语法渲染成html
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         # 包含收缩、表格等常用扩展
                                         # 'markdown.extensions.extra',
                                         # 语法高亮扩展
                                         'markdown.extensions.codehilite',
                                     ])

    context = {'article': article}
    return render(request, 'article/detail.html', context)
