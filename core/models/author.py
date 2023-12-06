from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя автора")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия автора")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
