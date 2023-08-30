from django.db import models


class Blogpost(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображение')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.title}, {self.date_published}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
