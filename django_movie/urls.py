"""django_movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from myapp.views import *
from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', HomeView.as_view(), name='home'),
    url('movie-item/', MovieDetail.as_view(), name='movie_detail'),
    url('^sort/$', SortView.as_view(), name='sort'),
    url('^publishcomment/', PublishCommentView.as_view(), name = 'publishcomment'),
    url('^favorate/', FavorateView.as_view(), name = 'favorate'),
    url('^users/', include('custom_user.urls', namespace = "users")),
    url('^blog/', include('blog.urls', namespace = 'blog')),
    url('^search/',views.search,name='search'),
]

from django.views.static import serve
from .settings import MEDIA_ROOT
urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),]