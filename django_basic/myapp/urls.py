from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    # どのURLで、どのビューを呼ぶかを登録する
    # path関数の第一引数は、どのURLか
    # 第二引数が、どのビューを呼ぶか
    path('', views.hello, name='hello'),
    path('home/', views.home, name='home'),
]