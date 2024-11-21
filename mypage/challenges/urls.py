from django.urls import path 

from . import views     # same folder import

urlpatterns = [
    # path("january", views.january),
    # path('february', views.february),
    path("", views.index, name="index"),   # /challenges/  这就是app主页
    path('<int:month>',views.monthlychallenge_by_num),
    path('<str:month>',views.monthlychallenge, name = 'month-challenge')
]   
# url config. Connect requests to views.
# 顺序很重要