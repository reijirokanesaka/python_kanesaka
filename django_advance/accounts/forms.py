from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class MyUserCreationForm(UserCreationForm):
    # UserCreationFormは、モデルフォームとして作られている
    # class Metaの部分を私たちで上書きする
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'is_active','age')
