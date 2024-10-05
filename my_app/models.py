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

    """наследуем Model и применяем к нему метод models чтобы Django перевел данные в SQL-тип"""
    title = models.CharField(
        max_length=150,
        verbose_name='Название')

    # image = models.ImageField(
    #     blank=True,
    #     upload_to='images/')

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