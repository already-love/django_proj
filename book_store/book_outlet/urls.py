from django.urls import path

from . import views

urlpatterns=[
    path("",views.index),
    path("<slug:slug>",views.book_detail, name="book-detail")  #这个name传入了index.html中
]     # <a href="{% url "book-detail" book.id %}> 作为链接