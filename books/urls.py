from django.urls import path
from .views import *

urlpatterns = [
    path("categories/",list_category.as_view()),
    path("cat/create/",create_category.as_view()),
    path("cat/update/<int:pk>/",update_category.as_view()),
    path("cat/delete/<int:pk>/",delete_category.as_view()),
    path("cat/detail/<int:pk>/",detail_category.as_view()),

    path("books/",list_book.as_view()),
    path("book/create/",create_book.as_view()),
    path("book/update/<int:pk>/",update_book.as_view()),
    path("book/delete/<int:pk>/",delete_book.as_view()),
    path("book/detail/<int:pk>/",detail_book.as_view()),

    path("trades/",list_trade.as_view()),
    path("trade/create/",create_trade.as_view()),
    path("trade/update/<int:pk>/",update_trade.as_view()),
    path("trade/delete/<int:pk>/",delete_trade.as_view()),
    path("trade/detail/<int:pk>/",detail_trade.as_view()),
]
