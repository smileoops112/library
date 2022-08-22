from django.db import models
from django.urls import reverse
import uuid


class Genre(models.Model):

    name = models.CharField(max_length=200, help_text='Введите жанр книги')

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=70)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Описание книги')
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
    )
    genre = models.ManyToManyField(Genre, help_text='Выберите жанр книги')

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-info', args=[str(self.id)])


class BookInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Уникальный id для книги')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    inprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    STATUS = (
        ('о', 'Обслуживание'),
        ('к', 'В кредит'),
        ('д', 'Доступный'),
        ('з', 'Зарезервированный'),
    )
    status = models.CharField(max_length=1, choices=STATUS, default='о', blank=True)

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id}, {self.book.title}'


class Author(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_day = models.DateField(null=True, blank=True)
    die_day = models.DateField('Die', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-info', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
