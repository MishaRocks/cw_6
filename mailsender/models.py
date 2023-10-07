from django.conf import settings
from django.db import models

NULLABLE = {
    "null": True,
    "blank": True
    }


class Message(models.Model):
    title = models.CharField(max_length=200, verbose_name='Тема письма')
    content = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Сообщение',
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):
    frequency_var = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    ]
    status_var = [
        ('create', 'создана'),
        ('started', 'запущена'),
        ('ended', 'завершена')
    ]
    send_time = models.TimeField(verbose_name='Время рассылки')
    frequency = models.IntegerField(**NULLABLE, verbose_name='Периодичность')
    status = models.CharField(max_length=10, choices=status_var, default='create', verbose_name='Статус')
    recipients = models.ManyToManyField('clients.Client', verbose_name='Получатель',  **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Автор', **NULLABLE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='активно')

    def __str__(self):
        return f'{self.status}'

    class Meta:
        verbose_name = 'Рассылка',
        verbose_name_plural = 'Рассылки'
