from django.contrib.auth.forms import AuthenticationForm
from django import forms



class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class SignupForm(forms.Form):
    """ユーザーの登録用のフォーム"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


    first_name = forms.CharField(
        label = 'ユーザー名（ファーストネーム）',
        max_length = 255,
    )

    last_name = forms.CharField(
        label = 'ユーザー名（ラストネーム）',
        max_length = 255,
    )

    email = forms.EmailField(
        label = 'Eメール',
        max_length = 255,
    )

    password = forms.CharField(
        label = 'パスワード',
        strip = False,
        widget = forms.PasswordInput(render_value = True)
    )