from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Book

from django.core.paginator import Paginator

def home(request):
    books = Book.objects.all()

    paginator = Paginator(books, 6)   # по 6 книг на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {
        'page_obj': page_obj
    })

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)

    return render(request, 'book_detail.html', {
        'book': book
    })


# Create your views here.
