from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ArticlePost
from .forms import ArticlePostForm
from django.contrib.auth.models import User
import markdown


# 博客主页
def article_list(request):
    # 取出所有文章
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html', context)


# 文章详情页
def article_detail(request, article_id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=article_id)

    # 将markdown语法渲染成html
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         # 包含收缩、表格等常用扩展
                                         'markdown.extensions.extra',
                                         # 语法高亮扩展
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])

    context = {'article': article}
    return render(request, 'article/detail.html', context)


# 写文章
def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据,暂不提交到数据库
            new_article = article_post_form.save(commit=False)
            # 指定用户id=1为作者
            new_article.author = User.objects.get(id=1)
            # 将数据提交到数据库中
            new_article.save()
            # 完成后返回文章列表
            return redirect("article:article_list")
        else:
            # 如果数据不合法，返回错误提示
            return HttpResponse("表单内容有误，请重新填写")
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)


# 删除文章
def article_delete(request, article_id):
    # 获取出相应的文章
    article = ArticlePost.objects.get(id=article_id)
    # 删除相应的文章
    article.delete()
    # 删除后返回文章列表
    return redirect('article:article_list')


# 编辑文章
def article_update(request, article_id):
    # 获取需要修改的具体文章对象
    article = ArticlePost.objects.get(id=article_id)
    # 判断用户是否POST提交数据
    if request.method == "POST":
        # 将提交的数据赋值到实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            # 将数据提交到数据库中
            article.save()
            # 完成后返回文章列表
            return article_detail(request, article_id)
        else:
            # 如果数据不合法，返回错误提示
            return HttpResponse("表单内容有误，请重新填写")
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = {'article': article, 'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)
