from django.shortcuts import render
from .models import *


def index(request):
    num_books = Book.objects.all()
    num_instance = BookInstance.objects.all().count()
    num_instance_avi = BookInstance.objects.filter(status__exact='д').count()
    num_authors = Author.objects.count()
    genre = Genre.objects.filter().count()
    book_count = Book.objects.count()
    return render(request, 'index.html', context={
        'num_books': num_books,
        'num_instance': num_instance,
        'num_instance_avi': num_instance_avi,
        'num_authors': num_authors,
        'genre': genre,
        'book_count': book_count
    })