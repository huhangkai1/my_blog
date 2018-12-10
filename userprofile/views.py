from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout


# 登录页
def user_login(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到实例中
        user_login_form = UserLoginForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if user_login_form.is_valid():
            # 清洗出合法数据
            data = user_login_form.cleaned_data
            print('data=', data)
            # 匹配账号密码是否正确
            user = authenticate(username=data['username'], password=data['password'])
            # 如果账号密码正确，保存密码到session中，跳转到文章列表页，否则返回错误
            if user:
                login(request, user)
                return redirect("article:article_list")
            else:
                return HttpResponse("账号或密码有误，请重新填写")
        else:
            # 如果数据不合法，返回错误提示
            return HttpResponse("账号或密码输入不合法，请重新填写")
    elif request.method == 'GET':
        # 创建表单类实例
        user_login_form = UserLoginForm()
        # 赋值上下文
        context = {'form': user_login_form}
        return render(request, 'userprofile/login.html', context)
    return HttpResponse("请使用post或get请求数据")


# 退出登录
def user_logout(request):
    logout(request)
    return redirect("article:article_list")

