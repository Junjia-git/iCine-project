#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.0.0.0'


from django.conf.urls import url
from .views import RegisterView, LoginView, LogoutView,DetailView

app_name = 'users'
urlpatterns = [
    url('register/', RegisterView.as_view(), name="register"),
    url('login/', LoginView.as_view(), name="login"),
    url('logout/', LogoutView.as_view(), name="logout"),
    url('detail/', DetailView.as_view(), name="detail"),

]