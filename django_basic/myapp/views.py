from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
def hello(request):
    return HttpResponse('Hello')

def home(request):
    return render(request, 'myapp/home.html')

def home2(request):
    context = {
        'title': 'ホーム2です',
    }
    return render(request, 'myapp/home2.html', context)

# TemplateViewは、htmlを単純に表示するのに使う
class Home(generic.TemplateView):
    template_name = 'myapp/home2.html'

    # テンプレートファイルに、追加で渡したいデータがあるときは
    # このメソッドを呼ぶ
    def get_context_data(self, **kwargs):
        # このメソッド上書きのときは、毎回super()で親のメソッドを呼ぶこと
        context = super().get_context_data(**kwargs)

        # 辞書[キー名] = 値 形式で、追加のデータを渡す
        context['title'] = 'ホーム2です'
        return context