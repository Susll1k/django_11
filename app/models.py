from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    published_date = models.DateField(verbose_name='Дата публикации')
    isbn = models.CharField(max_length=13, unique=True, verbose_name='ISBN')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title