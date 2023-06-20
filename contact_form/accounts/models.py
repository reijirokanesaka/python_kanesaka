from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_received_email = models.BooleanField('お問い合わせメールを受け取るか', default=True)
