from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg, Max, Min

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-title")   #减号代表desc。这步是数据库在做，不是python在做
    num_books = books.count()
    rating_data = books.aggregate(Avg("rating"), Max("rating"), Min("rating"))

    return render(request, "book_outlet/index.html", {
        "books":books,
        "total_number_of_books":num_books,
        "rating_data":rating_data,
    })   # request后面接着的是对应template，第三个参数是传入一个dict给这个template

def book_detail(request, slug):       #id是从urls那里传进来的。
    try:
        book = Book.objects.get(slug=slug)  # primary key
    except:
        raise Http404()
    # book = get_object_or_404(Book, pk=id)
    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling":book.is_bestselling,
    }) # request，紧接着的是对应template，第三个参数是传入一个dict给这个template

