from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User
from .book import Book


class Feedback(models.Model):
    book = models.ForeignKey(
        to=Book,
        on_delete=models.PROTECT,
        related_name="feedback",
        verbose_name="На книгу",
    )
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name='feedback',
        verbose_name="Кем оставлен отзыв",
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Рейтинг",
    )
    feedback_text = models.TextField(verbose_name="Текст отзыва")

    def __str__(self):
        return f"Отзыв {self.created_by.email} на {self.book.name}"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        unique_together = [['book', 'created_by']]
