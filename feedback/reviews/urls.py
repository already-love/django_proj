# 本页是新建的
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),     #从views.py里面拿了review这个函数
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view()),
]