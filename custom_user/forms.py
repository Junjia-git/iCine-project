#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.0.0.0'


import re
from django import forms
from django.core.exceptions import ValidationError


def mobile_validate(value):
    mobile_re = re.compile('^[0-9]{10}$')
    if not mobile_re.match(value):
        raise ValidationError('Phone Number Not Valid!')


class RegisterForm(forms.Form):
    uname = forms.CharField(required=True, error_messages={"invalid": u"User Name Invalid", "required": "User Name Required!"})
    email = forms.EmailField(required=True, error_messages={"invalid": u"E-mail Address Invalid", "required": "E-mail Required!"})
    mobile = forms.CharField(required = False, validators=[mobile_validate, ], error_messages = {"required": "Invalid Phone Number!"})
    pwd = forms.CharField(required=True, min_length=6, error_messages={"invalid": u"Minimum 6 character required！",
                                                                       "required": "Password Required！"})


class LoginForm(forms.Form):
    uname = forms.CharField(required=True)
    pwd = forms.CharField(required=True, min_length=6)

