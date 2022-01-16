from django.urls import path

from .views import BooksApiView

app_name = 'books_api'

urlpatterns = [
    path('api/books/', BooksApiView.as_view(), name='home-api'),
]
