from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from .serailizer import *

class list_category(ListAPIView):
    queryset=Category.objects.all()
    serializer_class = CategorySerailizer


class create_category(CreateAPIView):
    queryset=Category.objects.all()
    serializer_class = CategorySerailizer


class detail_category(RetrieveAPIView):
    queryset=Category.objects.all()
    serializer_class = CategorySerailizer


class update_category(UpdateAPIView):
    queryset=Category.objects.all()
    serializer_class = CategorySerailizer

class delete_category(DestroyAPIView):
    queryset=Category.objects.all()
    serializer_class = CategorySerailizer



class list_book(ListAPIView):
    queryset=Books.objects.all().order_by(title="title")
    serializer_class = BookSerailizer


class create_book(CreateAPIView):
    queryset=Books.objects.all()
    serializer_class = BookSerailizer


class detail_book(RetrieveAPIView):
    queryset=Books.objects.all()
    serializer_class = BookSerailizer


class update_book(UpdateAPIView):
    queryset=Books.objects.all()
    serializer_class = BookSerailizer

class delete_book(DestroyAPIView):
    queryset=Books.objects.all()
    serializer_class = BookSerailizer




class list_trade(ListAPIView):
    queryset=Trade.objects.all()
    serializer_class = TradeSerailizer


class create_trade(CreateAPIView):
    queryset=Trade.objects.all()
    serializer_class = TradeSerailizer


class detail_trade(RetrieveAPIView):
    queryset=Trade.objects.all()
    serializer_class = TradeSerailizer


class update_trade(UpdateAPIView):
    queryset=Trade.objects.all()
    serializer_class = TradeSerailizer

class delete_trade(DestroyAPIView):
    queryset=Trade.objects.all()
    serializer_class = TradeSerailizer