from django.db import models

from mailsender.models import NULLABLE


class Client(models.Model):
    email = models.EmailField(verbose_name='Email')
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    letters = models.ManyToManyField('mailsender.Mailing', verbose_name='Рассылка',  **NULLABLE)

    def __str__(self):
        return f'{self.email} ({self.name} {self.surname})'

    class Meta:
        verbose_name = 'Клиент',
        verbose_name_plural = 'Клиенты'
