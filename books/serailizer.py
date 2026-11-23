from rest_framework import serializers
from .models import *

class CategorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class TradeSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = "__all__"

