from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Article, Tag, Comment
from django.urls import reverse_lazy
from .forms import ArticleCreateForm, ArticleUpdateForm,SearchForm, CommentCreateForm
from django.db.models import Q

class Home(generic.TemplateView):
    template_name = 'blog/home.html'

class ArticleListView(generic.ListView):
    model = Article
    template_name = 'blog/article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        form = SearchForm(self.request.GET)
        form.is_valid()
        keyword = form.cleaned_data.get('keyword')
        if keyword:
            queryset = queryset.filter(
                # 記事のタイトルか、本文のどちらかにキーワードが含まれているものを絞り込む
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset


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

class CommentCreateView(generic.CreateView):
        model = Comment
        template_name = 'blog/comment_create.html'
        success_url = reverse_lazy('blog:home')
        form_class = CommentCreateForm


def form_valid(self, form):
    # form.save(commit=False) データベースにはまだ保存しない
    # commit=Falseビューで、モデルのフィールドを埋めるために使う引数
    comment = form.save(commit=False)

    # Commentモデルの、targetフィールドをここで埋める
    # モデル名.objects.get(フィールド=値)  1つだけ、DBから取り出すのに使うのがget
    # url内の<int:pk>は、self.kwargs['pk'] で取得できる
    comment.target = Article.objects.get(pk=self.kwargs['pk'])

    comment.save()  # saveしないと保存されない
    return redirect('blog:home')