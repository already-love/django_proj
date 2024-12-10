# 本页是新建的
from django.urls import path
from . import views

urlpatterns = [
    path("", views.review),     #从views.py里面拿了review这个函数
    path("thank-you", views.thank_you)
]