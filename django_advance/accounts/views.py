from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm
from .models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView

class AccountCreateView(generic.CreateView):
    Model = CustomUser
    form_class = MyUserCreationForm  # ユーザー作成するための、提供されているフォーム
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('accounts:create')

class Login(LoginView):
    template_name = 'accounts/login.html'

class Logout(LogoutView):
    # next_page = '/accounts/login/'
    # ログアウト後に、移動するページ
    next_page = reverse_lazy('accounts:login')


class Home(generic.TemplateView):
    template_name = 'accounts/home.html'

# Create your views here.
