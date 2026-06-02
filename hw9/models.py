from django.db import models
from django.core.validators import MinValueValidator
import datetime

class Reader(models.Model):
    """Информация о читателе"""
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Контактный телефон")
    email = models.EmailField(unique=True, verbose_name="Email")
    registration_date = models.DateField(default=datetime.date.today, verbose_name="Дата записи в библиотеку")

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    """Информация о книге"""
    title = models.CharField(max_length=255, verbose_name="Название книги")
    author = models.CharField(max_length=255, verbose_name="Автор")
    published_year = models.PositiveIntegerField(verbose_name="Год издания")
    style = models.CharField(max_length=100, verbose_name="Стиль / Жанр")
    publisher = models.CharField(max_length=255, verbose_name="Издательство")
    
    current_reader = models.ForeignKey(
        Reader, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="borrowed_books",
        verbose_name="У какого читателя находится"
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def is_available(self):
        """Проверка наличия книги в библиотеке"""
        return self.current_reader is None
    is_available.boolean = True
    is_available.short_description = "В наличии"

    def __str__(self):
        return self.title
