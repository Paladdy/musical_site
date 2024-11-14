
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class PostStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name='Статус публикации')
    code = models.CharField(max_length=2, verbose_name='Код статуса')

    def __str__(self):
        return self.name
    """Open Close Principal"""

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Поле для цены


    def __str__(self):
        return self.name


class KeySong(models.Model):

    # image = models.ImageField(
    #     upload_to='images/rain_1',  # Папка для хранения изображений
    #     blank=True,
    #     verbose_name='Изображение') # ошибка, связанная с отображением + миграциями

    """Наследуем Model и применяем к нему метод models чтобы Django перевел данные в SQL-тип"""
    title = models.CharField(
        max_length=150,
        verbose_name='Название')

    description = models.TextField(
        verbose_name='Описание трека')

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена')

    published = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата публикации')

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания')

    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления')

    slug = models.SlugField(
        max_length=150,
        unique=True,
        verbose_name='Слаг')
    """Для девелопера"""

    status = models.ForeignKey(PostStatus, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Позволяет сформировать более понятную slug-ссылку с элементами из БД в браузере с годом и слагом"""
        """селфами вытягивает поля из модели KeySong pusbleshed и slug"""
        return reverse(viewname='musical_site:song_post_detail', args=[self.published.year, self.slug])

class Comment(models.Model):
    song = models.ForeignKey(KeySong, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    # def __str__(self):
    #     return f'Comment by {self.author}'