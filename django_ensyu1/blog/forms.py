from django import forms
from .models import Article, Tag, Comment


class ArticleCreateForm(forms.ModelForm):

    class Meta:
        model = Article
        # ページに表示したいモデルのフィールドを、文字列で書きます
        fields = ('title','text','created_at','category','tags',)

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','text','created_at','category','tags',)

class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', required=False)

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','text',) # targetフィールドを含めない