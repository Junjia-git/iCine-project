# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import Group
from .forms import RegisterForm, LoginForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.core.files.base import ContentFile
from myapp.models import FavorateModel


# Create your views here.
class RegisterView(View):

    def get(self, request):
        return render(request, "register.html", {"request": request})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("uname")
            if UserProfile.objects.filter(username=user_name):
                return render(request, "register.html", {"register_form": register_form, "msg": "User already existed"})
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            pwd = request.POST.get("pwd")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = email
            user_profile.mobile = mobile
            user_profile.is_active = True
            user_profile.set_password(pwd)
            user_profile.save()
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form,"request": request})


class LogoutView(View):
    """
    User Logout
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("home"))


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {"request": request})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("uname", "")
            pass_word = request.POST.get("pwd", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("home"))
                else:
                    return render(request, "login.html", {"msg": "User not activated！"})
            else:
                return render(request, "login.html", {"msg": "User name or password error！"})
        else:
            return render(request, "login.html", {"login_form": login_form, "request": request})


class DetailView(View):

    def get(self, request):
        favorate_list = FavorateModel.objects.filter(person=request.user)
        return render(request, "detail.html", {"request": request, "favorate_list": favorate_list})


    def post(self, request):
        user_id = request.POST.get("id")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        obj = UserProfile.objects.get(id=int(user_id))
        obj.location = address
        obj.mobile = phone
        obj.email = email
        obj.save()
        return HttpResponseRedirect(reverse("users:detail"))


# modify avatar
class ChangeAvatarView(View):

    def post(self, request):
        obj = UserProfile.objects.get(id=request.user.id)
        pic = ContentFile(request.FILES['file'].read())
        obj.image.save(request.FILES['file'].name, pic)
        obj.save()
        return HttpResponse(json.dumps({'code':0, "avatar": obj.image.url}))


# reset password
class ResetPasswordView(View):
    def post(self, request):
        obj = UserProfile.objects.get(id=request.user.id)
        password = request.POST.get("password")
        obj.set_password(password)
        obj.save()
        return HttpResponse(json.dumps({'code':0, "avatar": obj.image.url}), content_type="application/json")





