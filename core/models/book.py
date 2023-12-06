from django.db import models
from users.models import User
from .genre import Genre
from .author import Author


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название книги")

    genre = models.ManyToManyField(
        to=Genre,
        related_name='book',
        verbose_name="Жанр(ы)"
    )

    author = models.ManyToManyField(
        to=Author,
        related_name='book',
        verbose_name="Автор(ы)"
    )

    publicated_date = models.DateField(verbose_name="Дата публикации")

    favorite_for = models.ManyToManyField(
        to=User,
        related_name="favorite_book",
        verbose_name="Избранное у пользователей",
        blank=True,
    )

    description = models.TextField(
        verbose_name="Описание",
        null=True, blank=False,
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
