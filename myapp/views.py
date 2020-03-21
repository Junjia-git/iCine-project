from django.shortcuts import render
import json
import datetime
from django.shortcuts import render
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from myapp.bing_search import run_query

# Create your views here.


class LoginRequiredMixin(object):
    """
    Login required，jump to login url
    """
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/users/login')


class HomeView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

    def get(self, request):
        recent_movie_list = MovieModel.objects.order_by("-publish_time")[:10]
        recommend_movie_list =  MovieModel.objects.order_by("-star")[:10]
        return render(request, 'index.html',{"recent_movie_list":recent_movie_list,
                                             "recommend_movie_list": recommend_movie_list})

class SortView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(SortView, self).dispatch(*args, **kwargs)

    def get(self, request):
        _type=request.GET.get("_type")
        title = request.GET.get("title")
        option_list = ClassifyModel.objects.all()
        movie_list = MovieModel.objects.all()
        if _type:
            movie_list = movie_list.filter(classify__name=_type)
        if title:
            movie_list = movie_list.filter(name__contains=title)
        return render(request, 'sort.html', {"movie_list": movie_list, "option_list": option_list})


class MovieDetail(View):
    def get(self, request):
        movie_id = int(request.GET.get("id"))
        item = MovieModel.objects.get(id = movie_id)
        return render(request, 'movie_item.html', {'item': item})


class PublishCommentView(LoginRequiredMixin, View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(PublishCommentView, self).dispatch(*args, **kwargs)

    def post(self, request):
        try:
            uid = int(request.POST["id"])
            movie = MovieModel.objects.get(id=uid)
            content = request.POST['content']
            score = request.POST['score']
            CommentModel.objects.create(person=request.user, content=content, create_time=datetime.datetime.now(),
                                        movie=movie, score=float(score))
            return HttpResponse(json.dumps({"err": 0}), content_type='application/json')
        except Exception as e:
            raise Http404

class FavorateView(LoginRequiredMixin, View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(FavorateView, self).dispatch(*args, **kwargs)

    def post(self, request):
        try:
            uid = int(request.POST["id"])
            movie = MovieModel.objects.get(id=uid)
            FavorateModel.objects.create(person=request.user,  create_time=datetime.datetime.now(),
                                        movie=movie)
            return HttpResponse(json.dumps({"err": 0}), content_type='application/json')
        except Exception as e:
            raise Http404

def search(request):
    result_list=[]

    if request.method == 'POST':
        query = request.POST['query'].strip() 
        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)
    
    return render(request, 'search.html', {'result_list': result_list})