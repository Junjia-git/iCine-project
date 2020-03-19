#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.0.0.0'


from django.conf.urls import url
from .views import RegisterView, LoginView, LogoutView,DetailView,ChangeAvatarView,ResetPasswordView

app_name = 'users'
urlpatterns = [
    url('register/', RegisterView.as_view(), name="register"),
    url('login/', LoginView.as_view(), name="login"),
    url('logout/', LogoutView.as_view(), name="logout"),
    url('detail/', DetailView.as_view(), name="detail"),
    url('change-avatar/', ChangeAvatarView.as_view(), name='change-avatar'),
    url('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]