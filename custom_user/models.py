# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name = "Phone Number")
    image = models.ImageField(upload_to="img", default=u"image/default.png", max_length=100)
    wechat = models.CharField(max_length=11, null=True, blank=True, verbose_name="FaceBook ID")
    location = models.CharField(max_length=11, null=True, blank=True, verbose_name="Address")

    class Meta:
        verbose_name = "User Information"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
