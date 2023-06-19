from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Userモデルにもともとあるが、ユニークにしたいので、emailフィールドを上書き
    email = models.EmailField('メールアドレス', unique=True)

    # Userモデルにないフィールドを追加している
    age = models.PositiveIntegerField('年齢')

    REQUIRED_FIELDS = ['age', 'email']
