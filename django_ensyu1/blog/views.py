from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Article, Tag

class Home(generic.TemplateView):
    template_name = 'blog/home.html'

class ArticleListView(generic.ListView):
    model = Article
    template_name = 'blog/article_list.html'

class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

class TagListView(generic.ListView):
    model = Tag
    template_name = 'blog/tag_list.html'


# Create your views here.
