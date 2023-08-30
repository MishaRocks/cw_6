from django.db import models

from mailsender.models import NULLABLE


class Logs(models.Model):
    last_try = models.DateTimeField(verbose_name='Последняя попытка', **NULLABLE)
    status = models.CharField(**NULLABLE, verbose_name='Статус')
    server_ans = models.CharField(**NULLABLE, verbose_name='Ответ сервера')

    def __str__(self):
        return f'{self.server_ans}'

    class Meta:
        verbose_name = 'Лог',
        verbose_name_plural = 'Логи'
