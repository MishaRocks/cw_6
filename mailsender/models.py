from django.db import models

NULLABLE = {
    "null": True,
    "blank": True
    }


class Client(models.Model):
    email = models.EmailField(verbose_name='Email')
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.email} ({self.name} {self.surname})'

    class Meta:
        verbose_name = 'Клиент',
        verbose_name_plural = 'Клиенты'


class Mailing(models.Model):
    send_time = models.DateTimeField(verbose_name='Время рассылки')
    frequency = models.IntegerField(**NULLABLE, verbose_name='Периодичность')
    status = models.CharField(default='Создана', verbose_name='Статус')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Клиент')

    def __str__(self):
        return f'{self.status}'

    class Meta:
        verbose_name = 'Рассылка',
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    title = models.CharField(max_length=200, verbose_name='Тема письма')
    content = models.TextField(verbose_name='Тело письма')
    mailing = models.ForeignKey('Mailing', on_delete=models.RESTRICT, verbose_name='Рассылка')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Сообщение',
        verbose_name_plural = 'Сообщения'


class Logs(models.Model):
    last_try = models.DateTimeField(verbose_name='Последняя попытка', **NULLABLE)
    status = models.CharField(**NULLABLE, verbose_name='Статус')
    server_ans = models.CharField(**NULLABLE, verbose_name='Ответ сервера')
    message = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name='Рассылка')

    def __str__(self):
        return f'{self.server_ans}'

    class Meta:
        verbose_name = 'Лог',
        verbose_name_plural = 'Логи'
