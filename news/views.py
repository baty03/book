from django.shortcuts import render, get_object_or_404
from .models import Book


def home(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)

    return render(request, 'book_detail.html', {
        'book': book
    })
# Create your views here.
