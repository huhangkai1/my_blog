from django.db import models
# 导入内建的User模型
from django.contrib.auth.models import User
# timezone 处理时间相关的事务、
from django.utils import timezone




# 博客的文章数据模型
class ArticlePost(models.Model):

    # 文章作者。参数 on_delete 用于指定数据删除的方式，避免两个关联的数据不一致。
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题。models.CharField 保存较短的字符串，如标题。
    title = models.CharField(max_length=100)

    # 文章正文。保存大量文本用 models.TextField。
    body = models.TextField()

    # 分类


    # 浏览量

    # 文章创建时间。参数default=timezone.now 指定创建参数时默认写入当前时间。
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间。参数auto_now=True 指定每次数据更新时写入当前时间。
    updated = models.DateTimeField(auto_now=True)

    # 内部类，定义元数据
    class Meta:
        # ordering 定义数据的排列顺序，-表示倒叙排列
        ordering = ('-created',)

    # 函数__str__ 定义对象调用str() 方法时的返回值内容
    def __str__(self):
        # 将文章的标题返回
        return self.title
