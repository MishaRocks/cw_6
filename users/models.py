from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=50, verbose_name='Имя')
    is_email_verified = models.BooleanField(default=False, verbose_name='Подтверждение почты')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'Пользователь',
        verbose_name_plural = 'Пользователи'
