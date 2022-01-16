from rest_framework import serializers

from list_of_books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'title', 'authors', 'published_date', 'ISBN_number', 'page_count', 'thumbnail', 'language'
        )
