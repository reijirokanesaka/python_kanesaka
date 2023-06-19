from django import forms
from .models import Article


class ArticleCreateForm(forms.ModelForm):

    class Meta:
        model = Article
        # ページに表示したいモデルのフィールドを、文字列で書きます
        fields = ('title','text','created_at','category','tags',)

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','text','created_at','category','tags',)