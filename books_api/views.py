from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from list_of_books.models import Book
from .serializers import BookSerializer


class BooksApiView(APIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    @staticmethod
    def get_pub_date_range(published_date):
        published_date = Book.objects.filter(published_date__range=published_date)
        serializer = BookSerializer(published_date, many=True)
        return serializer

    @staticmethod
    def get_authors(author):
        author = Book.objects.filter(authors__icontains=author)
        serializer = BookSerializer(author, many=True)
        return serializer

    @staticmethod
    def get_language(language):
        language = Book.objects.filter(language__icontains=language)
        serializer = BookSerializer(language, many=True)
        return serializer

    def get(self, request):
        published_date = request.query_params.getlist('published_date')
        author = request.query_params.get('author')
        language = request.query_params.get('language')
        if published_date:
            serializer = self.get_pub_date_range(published_date)
        elif author:
            serializer = self.get_authors(author)
        elif language:
            serializer = self.get_language(language)
        else:
            books = self.get_queryset()
            serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
