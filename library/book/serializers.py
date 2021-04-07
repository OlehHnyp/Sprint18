from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')


class BookViewAll(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'description')
