from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Article, Tag
from django.urls import reverse_lazy
from .forms import ArticleCreateForm, ArticleUpdateForm

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

class ArticleCreateView(generic.CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    success_url = reverse_lazy('blog:article_list')  # テンプレートで使った、urlタグみたいなもの
    form_class = ArticleCreateForm

class ArticleUpdate(generic.UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'blog/article_update.html'
    success_url = reverse_lazy('blog:article_list')

class ArticleDelete(generic.DeleteView):
    # フォームは必要なし
    model = Article
    template_name = 'blog/article_delete.html'
    success_url = reverse_lazy('blog:article_list')

# Create your views here.
