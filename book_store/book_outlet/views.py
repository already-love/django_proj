from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books":books 
    })   # request后面接着的是对应template，第三个参数是传入一个dict给这个template

def book_detail(request, id):       #id是从urls那里传进来的。
    try:
        book = Book.objects.get(pk=id)  # primary key
    except:
        raise Http404()
    # book = get_object_or_404(Book, pk=id)
    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling":book.is_bestselling,
    }) # request，紧接着的是对应template，第三个参数是传入一个dict给这个template

