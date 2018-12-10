# 引入表单类
from django import forms
# 引入 User 模型
from django.contrib.auth.models import User


# 登录表单类
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# 注册表单类
class UserRegisterForm(forms.ModelForm):
    # 复写 user的密码
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    # 对两次密码一致性校验
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError('两次输入的密码不一致')
