# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm, SignupForm
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from .models import Content


class Top(generic.TemplateView):
    template_name = 'register/top.html'


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'register/login.html'


class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'register/top.html'


class Signup(FormView):
    """ユーザーの登録"""
    template_name = 'register/signup.html'
    success_url = '/login'
    form_class = SignupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SignupForm()
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()

        return super().form_valid(form)


def contents_list(request):
    contents = Content.objects.all()

    return render(request, 'content/contents_list.html', contents)