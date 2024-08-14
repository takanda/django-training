from rest_framework import serializers
from .models import Auther, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'published_at']

class AutherSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True, source='book_set')

    class Meta:
        model = Auther
        fields = ['name', 'books']